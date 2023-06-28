import 'dart:convert';
import 'package:bubble/bubble.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';
import 'package:url_launcher/url_launcher.dart';

var year = DateFormat('yyyy').format(DateTime.now());
var now_sender = DateTime.now();

class chat_bot extends StatefulWidget {
  const chat_bot({Key? key}) : super(key: key);

  @override
  State<chat_bot> createState() => chat_botState();
}

class chat_botState extends State<chat_bot> {
  final GlobalKey<AnimatedListState> _listkey = GlobalKey();
  final List<String> _data = [];

  static const String Bot_URL =
      'http://ivinbot.vivifyhealthcare.com:5005/webhooks/rest/webhook';
  TextEditingController querycontroller = TextEditingController();
  ScrollController scrollController = ScrollController();
  late ScrollController _scrollController;

  @override
  void initState() {
    _scrollController = ScrollController()
      ..addListener(() {
        setState(() {
          if (_scrollController.offset >= 400) {
          } else {}
        });
      });
    super.initState();
  }

  @override
  void dispose() {
    _scrollController.dispose(); // dispose the controller
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          centerTitle: true,
          backgroundColor: Colors.white,
          foregroundColor: Colors.black,
          title: const Text('IVIN'),
        ),
        body: Stack(
          children: <Widget>[
            AnimatedList(
              controller: _scrollController,
              scrollDirection: Axis.vertical,
              padding: const EdgeInsetsDirectional.only(bottom: 50.0),
              key: _listkey,
              itemBuilder:
                  (BuildContext context, int index, Animation animation) {
                return buildItem(_data[index], animation, index);
              },
            ),
            Align(
              alignment: Alignment.bottomCenter,
              child: ColorFiltered(
                colorFilter: const ColorFilter.linearToSrgbGamma(),
                child: Container(
                  color: Colors.white,
                  child: Padding(
                    padding: const EdgeInsets.only(left: 20, right: 20),
                    child: TextField(
                      controller: querycontroller,
                      textInputAction: TextInputAction.send,
                      onSubmitted: (msg) {
                        getrespose(msg, querycontroller.text);
                        querycontroller.clear();
                      },
                      decoration: const InputDecoration(
                          icon: Icon(Icons.message),
// madhu
                          hintText: 'Say "Hi" to start the conversation'),
                    ),
                  ),
                ),
              ),
            ),
            Align(
                alignment: Alignment.bottomRight,
                child: ElevatedButton(
                    onPressed: () {
                      getrespose(querycontroller.text, querycontroller.text);
                      querycontroller.clear();
                      _scrollController.animateTo(10000000,
                          duration: const Duration(seconds: 2),
                          curve: Curves.bounceIn);
                    },
                    child: const Icon(Icons.send)))
          ],
        ));
  }

  List response_list = [];

  getrespose(msg, name) async {
    print("msg");
    var x = name.toString().replaceAll('@', '');
    insertSingleItem(x.replaceAll('<bot>', ''));
    response_list.add('msg');

    var client = http.Client();
    var url = Uri.parse(Bot_URL);

    var dataMessage =
    jsonEncode({'message': msg, "sender": now_sender.toString()});
    var response = await client.post(url, body: dataMessage);
    print((response.statusCode));
    int lenRespo = ((jsonDecode(response.body)).length);
    var respo = jsonDecode(response.body);
    print(response.body);

    for (int i = 0; i < lenRespo; i++) {
      bool y = respo[i]['image'] != null;
      bool b = respo[i]['buttons'] != null;
      bool d = respo[i]['text'] != null;
      if (b == true) {
        List mm = respo[i]['buttons'];
        int mmLen = mm.length;
        response_list.add('${respo[i]['text']}<bot>');
        insertSingleItem("${respo[i]['text']}<bot>");
        for (int j = 0; j < mmLen; j++) {
          response_list.add('<intent>${respo[i]['buttons'][j]['payload']}');
          insertSingleItem("@${respo[i]['buttons'][j]['title']}<bot>");
          print((respo[i]['buttons']).length);
          print((respo[i]['buttons']).runtimeType);
        }
      } else if (y == true) {
        response_list.add('${respo[i]['image']}<bot>');
        insertSingleItem("${respo[i]['image']}<bot>");
      } else if (d != null) {
        response_list.add('${respo[i]['text']}<bot>');
        insertSingleItem("${respo[i]['text']}<bot>");
      }

      _scrollController.animateTo(10000000,
          duration: const Duration(seconds: 1), curve: Curves.bounceIn);
    }
  }

  void insertSingleItem(String mes) {
    _data.add(mes);
    _listkey.currentState?.insertItem(_data.length - 1);
  }

  http.Client getclient() {
    return http.Client();
  }

  Widget buildItem(String item, animation, int index) {
    bool mine = item.endsWith('<bot>');
    return Padding(
      padding: const EdgeInsets.all(2),
      child: Container(
          margin: const EdgeInsets.only(left: 15.0),
          alignment: mine ? Alignment.topLeft : Alignment.topRight,
          child: mine
              ? Container(
            color: mine ? Colors.white : Colors.blue,
            child: mg(item, index),
          )
              : Bubble(
            alignment: Alignment.topRight,
            color: Colors.white,
            child: mg(item, index),
          )),
    );
  }

  Widget mg(item, index) {
    bool img = item.startsWith('https');
    bool btn = item.startsWith('@');
    bool txt = item.startsWith('/');

    if (img == true) {
      return CachedNetworkImage(
          imageUrl: item.replaceAll('<bot>', ''),
          placeholder: (context, url) => const CircularProgressIndicator(),
          errorWidget: (context, url, error) => TextButton(
            onPressed: () {
              final uri = Uri.parse(url);
              _launchUrl(uri);
            },
            child: Text(url,
                style: const TextStyle(
                    decoration: TextDecoration.underline,
                    color: Colors.blue,
                    fontSize: 17.0)),
          ));
    } else if (btn == true) {
      var btnText = item.replaceAll('@', '');
      var btnText2 = (btnText.replaceAll('<bot>', ''));
      if (txt == false) {
        return ElevatedButton(
          onPressed: () {
            print(
                "button --- ${response_list[index].replaceAll('<intent>', '')}");
            getrespose(
                response_list[index].replaceAll('<intent>', ''), _data[index]);
            _scrollController.animateTo(10000,
                duration: const Duration(seconds: 5), curve: Curves.bounceIn);
          },
          style: ButtonStyle(
              overlayColor: MaterialStateProperty.resolveWith<Color?>(
                    (Set<MaterialState> states) {
                  if (states.contains(MaterialState.pressed)) {
                    return Colors.green.shade800;
                  }
                  return null;
                },
              ),
              backgroundColor:
              MaterialStateColor.resolveWith((states) => Colors.white),
              shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                  RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(23.0),
                      side: const BorderSide(color: Colors.lightBlueAccent)))),
          child: Text(
            btnText2,
            style: const TextStyle(
                color: Colors.blue, fontWeight: FontWeight.bold),
          ),
        );
      } else {
        return const Text('');
      }
    } else {
      return Padding(
        padding: const EdgeInsets.all(8.0),
        child: Text(
          item.replaceAll('<bot>', ''),
          style:
          const TextStyle(color: Colors.black, fontWeight: FontWeight.w500),
        ),
      );
    }
  }
}

Future<void> _launchUrl(url) async {
  if (!await launchUrl(url)) {
    throw Exception('Could not launch $url');
  }
}

meta_olevba.py
================

This module parses Java class files and extracts their constants pool tables, provides classes, and requires classes. It uses python-javatools. 
python-javatools can be accessed here: https://github.com/obriencj/python-javatools

Sample output
```
        "META_CLASS": {
          "Constants": {
            "50": "jar",
            "57": "java/lang/Exception",
            "17": "#47.#56",
            "47": "#68",
            "37": "AppletX.java",
            "74": "parseInt",
            "55": "#74:#75",
            "33": "LineNumberTable",
            "52": "lport",
            "53": "",
            "36": "SourceFile",
            "51": "lhost",
            "3": "#40",
            "35": "<clinit>",
            "1": "#21.#38",
            "41": "ACED00057372001B6A6176612E7574696C2E477265676F7269616E43616C656E6461728F3DD7D6E5B0D0C10200014A0010677265676F7269616E4375746F766572787200126A6176612E7574696C2E43616C656E646172E6EA4D1EC8DC5B8E03000B5A000C6172654669656C647353657449000E66697273744461794F665765656B5A0009697354696D655365745A00076C656E69656E744900166D696E696D616C44617973496E46697273745765656B4900096E6578745374616D7049001573657269616C56657273696F6E4F6E53747265616D4A000474696D655B00066669656C64737400025B495B000569735365747400025B5A4C00047A6F6E657400144C6A6176612F7574696C2F54696D655A6F6E653B78700100000001010100000001000000020000000100000121563AFC0E757200025B494DBA602676EAB2A502000078700000001100000001000007D9000000040000001500000004000000120000008A00000002000000030000000100000004000000100000001100000022000002DEFE488C0000000000757200025B5A578F203914B85DE20200007870000000110101010101010101010101010101010101737200186A6176612E7574696C2E53696D706C6554696D655A6F6E65FA675D60D15EF5A603001249000A647374536176696E6773490006656E6444617949000C656E644461794F665765656B490007656E644D6F6465490008656E644D6F6E7468490007656E6454696D6549000B656E6454696D654D6F64654900097261774F666673657449001573657269616C56657273696F6E4F6E53747265616D490008737461727444617949000E73746172744461794F665765656B49000973746172744D6F646549000A73746172744D6F6E7468490009737461727454696D6549000D737461727454696D654D6F64654900097374617274596561725A000B7573654461796C696768745B000B6D6F6E74684C656E6774687400025B42787200126A6176612E7574696C2E54696D655A6F6E6531B3E9F57744ACA10200014C000249447400124C6A6176612F6C616E672F537472696E673B787074000E416D65726963612F446177736F6E0036EE80000000000000000000000000000000000000000000000000FE488C00000000020000000000000000000000000000000000000000000000000000000000757200025B42ACF317F8060854E002000078700000000C1F1C1F1E1F1E1F1F1E1F1E1F770A000000060000000000007571007E0006000000020000000000000000787372000D6D73662E782E4C6F61646572585E8B4C67DDC409D8020000787078FFFFF4E2F964AC000A",
            "40": "java/io/ByteArrayInputStream",
            "43": "#62:#63",
            "42": "#61",
            "45": "#30:#65",
            "44": "#30:#64",
            "23": "J",
            "46": "#66:#67",
            "49": "#71:#72",
            "48": "#69:#70",
            "21": "#60",
            "20": "#59",
            "27": "serializedObject",
            "64": "([B)V",
            "63": "(Ljava/lang/String;)[B",
            "62": "StringToBytes",
            "61": "msf/x/PayloadX",
            "60": "java/applet/Applet",
            "29": "data",
            "28": "Ljava/lang/String;",
            "30": "<init>",
            "65": "(Ljava/io/InputStream;)V",
            "66": "readObject",
            "67": "()Ljava/lang/Object;",
            "68": "msf/x/LoaderX",
            "69": "instance",
            "34": "init",
            "24": "ConstantValue",
            "25": "-3238297386635759160l",
            "2": "#39",
            "5": "#42.#43",
            "4": "#41",
            "7": "#2.#45",
            "6": "#3.#44",
            "9": "#47.#48",
            "8": "#2.#46",
            "18": "#57",
            "13": "#51",
            "77": "(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;I)V",
            "76": "bootstrapPayload",
            "75": "(Ljava/lang/String;)I",
            "12": "#50",
            "73": "java/lang/Integer",
            "72": "(Ljava/lang/String;)Ljava/lang/String;",
            "71": "getParameter",
            "70": "Lmsf/x/LoaderX;",
            "15": "#53",
            "32": "Code",
            "58": "#29:#28",
            "11": "#20.#49",
            "10": "#29",
            "39": "java/io/ObjectInputStream",
            "38": "#30:#31",
            "59": "msf/x/AppletX",
            "22": "serialVersionUID",
            "14": "#52",
            "16": "#54.#55",
            "19": "#20.#58",
            "54": "#73",
            "31": "()V",
            "56": "#76:#77"
          },
          "Provides": [
            "msf.x.AppletX.<init>():void",
            "msf.x.AppletX.init():void",
            "msf.x.AppletX.data:java.lang.String",
            "msf.x.AppletX"
          ],
          "Requires": [
            "java.lang.Integer.parseInt(java.lang.String):int",
            "java.io.ByteArrayInputStream.<init>(byte[]):void",
            "msf.x.LoaderX.bootstrapPayload(java.lang.String,java.lang.String,java.lang.String,int):void",
            "msf.x.LoaderX.instance:msf.x.LoaderX",
            "java.io.ObjectInputStream.<init>(java.io.InputStream):void",
            "java.io.ByteArrayInputStream",
            "msf.x.LoaderX",
            "msf.x.PayloadX",
            "java.lang.Exception",
            "java.applet.Applet.<init>():void",
            "java.lang.Integer",
            "java.applet.Applet",
            "msf.x.PayloadX.StringToBytes(java.lang.String):byte[]",
            "java.io.ObjectInputStream.readObject():java.lang.Object",
            "java.io.ObjectInputStream",
            "msf.x.AppletX.getParameter(java.lang.String):java.lang.String"
          ]
        }
      },
```

Installation
---
* Install python-javatools (https://github.com/obriencj/python-javatools)
* Put meta_class.py in directory laikaboss/laikaboss/modules/
* Modify dispatch.yara to include the module
```
rule type_is_java_class
{
    meta:
        scan_modules = "META_CLASS"
        file_type = "class"
    condition:
        uint32(0) == 0xbebafeca
}
```

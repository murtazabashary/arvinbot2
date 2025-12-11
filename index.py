<?php
/*

📌 کانال ایلیا سورس
برای دریافت سورس های بیشتر به کانال ما سر بزنید :)
@Source_Eliya

*/
//==================================================
$time = date("H:i");
$url="ادرس هاست";
date_default_timezone_set('Asia/Tehran');
  $times = date('H:i');
  $enemy = file_get_contents('enemy.txt');
  $year = date('Y/m/d', time());
  $fosh = file_get_contents("$url/foshself.php");
  $smart = $MadelineProto->get_self();
  $admin = "ایدی عددی ادمین";
  //=================================================
  	if ((int)json_decode(file_get_contents('Config.json'))->Timename == 1) {
$MadelineProto->account->updateProfile(['first_name' => "ساعت | $times |"]);
}
if ((int)json_decode(file_get_contents('Config.json'))->Timebio == 1) {
$MadelineProto->account->updateProfile(['about' => "$times"]);
}
  if ($userID == $admin) {
 if($msg == "ربات"){
$MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' =>'Bot Is Online', 'parse_mode' => 'html' ]);
}

  	if(stristr($msg,'run ')){
    $cod = substr($msg, 4);
file_put_contents('co.php','<?php' . PHP_EOL . $cod);
$b = file_get_contents("$url/co.php");
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message'=> "**CODE:**
`$cod`

**RESULT:**
`$b`", 'parse_mode' => 'markdown']);
}
      if ($msg == "markread on") {
 $Conf = json_decode(file_get_contents('Config.json'));
 $Conf->Markread = 1;
 file_put_contents('Config.json', json_encode($Conf));
 $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => '• sᴇʟғ ᴛʏᴘɪɴɢ ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏɴ •', 'parse_mode' => 'MarkDown']);
      }
      if ($msg == "markread off") {
 $Conf = json_decode(file_get_contents('Config.json'));
 $Conf->Markread = 0;
 file_put_contents('Config.json', json_encode($Conf));
 $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' • sᴇʟғ ᴍᴀʀᴋʀᴇᴀᴅ  ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏғғ •', 'parse_mode' => 'MarkDown']);
      }

 if (strpos($msg, "clean") !== false) {
     if (!isset($update['update']['message']['reply_to_msg_id'])) {
$del = str_replace("clean", "", $msg);
if (is_numeric($del)) {
    for ($i = $msg_id - 1; $i >= $msg_id - 1 - $del; $i--) {
        $MadelineProto->channels->deleteMessages(['channel' => $chatID, 'id' => [$i]]);
    }
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " • ɴᴜᴍʙᴇʀ $del ᴄʟᴇᴀʀᴇᴅ •
 ", 'parse_mode' => 'MarkDown']);
} else {
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "• ᴇʀᴏʀ
sᴇɴᴅ ᴛʜᴇ ɴᴜᴍʙᴇʀ •
", 'parse_mode' => 'MarkDown']);
}
     }
 }
     if ($msg == "online on") {
$Conf = json_decode(file_get_contents('Config.json'));
$Conf->Online = 1;
file_put_contents('Config.json', json_encode($Conf));
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => '• sᴇʟғ ᴏɴʟɪɴᴇ ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏɴ •', 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "online off") {
$Conf = json_decode(file_get_contents('Config.json'));
$Conf->Online = 0;
file_put_contents('Config.json', json_encode($Conf));
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' • sᴇʟғ ᴏɴʟɪɴᴇ  ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏғғ •', 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "poker on") {
$Conf = json_decode(file_get_contents('Config.json'));
$Conf->Poker = 1;
file_put_contents('Config.json', json_encode($Conf));
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " • sᴇʟғ ᴘᴏᴋᴇʀ ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏɴ •", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "me") {
$Slf = json_encode($MadelineProto->get_self());
$out = json_encode($smart, true);
$phone = $smart["phone"];
$first = $smart["firstname"];
$last_name = $MadelineProto->get_self()['last_name'];
$usern = $Slf["user_name"];
$idus = $smart["id"];
$my_name = $MadelineProto->get_self()['first_name'];
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "
first name : $my_name
last name : $last_name
User name : $usern
userid: $idus
 phone : +$phone ️", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "poker off") {
$Conf = json_decode(file_get_contents('Config.json'));
$Conf->Poker = 0;
file_put_contents('Config.json', json_encode($Conf));
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " • sᴇʟғ ᴘᴏᴋᴇʀ  ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏғғ •", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "help") {
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "➲ Hᴇʟᴘ SᴇʟF

#Aɴsᴡᴇʀ :

➲ Sᴇᴛᴀɴsᴡᴇʀ + Tᴇxᴛ | Tᴇxᴛ
➲ Dᴇʟᴀɴsᴡᴇʀ + Tᴇxᴛ
➲ Cʟᴇᴀɴ Aɴsᴡᴇʀs
➲ Aɴsᴡᴇʀʟɪsᴛ

#Eɴᴇᴍʏ :

➲ Eɴᴇᴍʏ ᴏɴ
➲ Eɴᴇᴍʏ ᴏғғ
➲ Sᴇᴛᴇɴᴇᴍʏ | UsᴇʀIᴅ ᴏʀ Rᴇᴘʟʏ
➲ Dᴇʟᴇɴᴇᴍʏ | UsᴇʀIᴅ ᴏʀ Rᴇᴘʟʏ
➲ Cʟᴇᴀɴᴇɴᴇᴍʏʟɪsᴛ
➲ Eɴᴇᴍʏʟɪsᴛ
➲ Nᴜᴍʙᴇʀ

#SᴜᴘᴇʀGʀᴏᴜᴘ :

➲ Cʟᴇᴀɴ +(1-1000)
➲ Dᴇʟ + Rᴇᴘʟʏ
➲ Bᴀɴ + ʀᴇᴘʟᴀʏ
➲ Tʀᴀɴsʟᴀᴛᴇ Rᴇᴘʟʏ+ғᴀ|ᴇɴ|ᴀʀ SᴜᴘᴇʀGʀᴏᴜᴘ
➲ Pɪɴ + ʀᴇᴘʟʏ
➲ Uɴᴘɪɴ

#Usᴇʀ :

➲ Rᴇᴍ (Rᴇᴘʟʏ) (JᴜsᴛPᴠ)
➲ ɪᴅ (Rᴇᴘʟʏ)
➲ Wᴇʙʜᴏᴏᴋ + ᴛᴏᴋᴇɴ + ᴀᴅᴅʀᴇs
➲ Mᴇ
➲ Pʀᴏғɪʟᴇ + Fɪʀsᴛɴᴀᴍᴇ | ʟᴀsᴛNᴀᴍᴇ | ᴛᴇxᴛʙɪᴏ
➲ Sᴇᴛᴜsᴇʀɴᴀᴍᴇ + Tᴇxᴛ
➲ Mᴀʀᴋʀᴇᴀᴅ ᴏɴ|ᴏғғ
➲ Tʏᴘɪɴɢ + ᴏɴ|ᴏғғ
➲ Pᴏᴋᴇʀ  + ᴏɴ|ᴏғғ
➲ Sᴛᴀᴛs
➲ Bʟᴏᴄᴋ + Usᴇʀɴᴀᴍᴇ
➲ Uɴʙʟᴏᴄᴋ + Usᴇʀɴᴀᴍᴇ
➲ Sᴇssɪᴏɴs
➲ Sᴜᴘ + ᴛᴇxᴛ

#Oᴛʜᴇʀ :

➲ Lɪᴋᴇ + Tᴇxᴛ
➲ ᴄᴏɴᴅɪᴛɪᴏɴ
➲ ʟᴇғᴛ
➲ Sᴀᴠᴇ
➲ Sᴘᴀᴍ + متن + تعداد
➲ Bʟᴜᴇ + اسم شما
➲ Hɪᴅᴅᴇɴ پیام خصوصی + ایدی عددی کاربر
➲ Sʜᴏʀᴛ + لینک شما
➲ Aᴘᴋ + اسم برنامه
➲ ᴄᴀʟᴄ عدد +یا- عدد
➲ Sᴛɪᴄᴋᴇʀ + متن
➲ Jᴏᴋᴇ
➲ Gᴏᴏɢʟᴇ + متنی ک میخای سرچ شه
➲ Gɪғ + موضوع گیف
➲ Pɪᴄ + موضوع عکس
➲ Vᴏɪᴄᴇ + متن ویس
", 'parse_mode' => 'MarkDown']);
     }
     if (preg_match("/^[\/\#\!]?(sessions)$/i", $msg)) {
$authorizations = $MadelineProto->account->getAuthorizations();
$txxt = "";
foreach ($authorizations['authorizations'] as $authorization) {
    $txxt .= "
■□■□■□■□■□■□■□■□■□■□■□■
hash: " . $authorization['hash'] . "
device_model: " . $authorization['device_model'] . "
platform: " . $authorization['platform'] . "
system_version: " . $authorization['system_version'] . "
api_id: " . $authorization['api_id'] . "
app_name: " . $authorization['app_name'] . "
app_version: " . $authorization['app_version'] . "
date_created: " . date("Y-m-d H:i:s", $authorization['date_active']) . "
date_active: " . date("Y-m-d H:i:s", $authorization['date_active']) . "
ip: " . $authorization['ip'] . "
country: " . $authorization['country'] . "
region: " . $authorization['region'] . "
■□■□■□■□■□■□■□■□■□■□■□■
";
}
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " **$txxt** ️", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
     }

     if (strpos($msg, "setenemy ") !== false) {
$prima = trim(str_replace("setenemy ", "", $msg));
$myfile2 = fopen("enemy.txt", "a") or die("Unable to open file!");
fwrite($myfile2, "$prima\n");
fclose($myfile2);
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " Usᴇʀ : $prima
 Is Nᴏᴡ Iɴ Eɴᴇᴍʏ Lɪsᴛ", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "setenemy") {
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $gmsg = $MadelineProto->messages->getMessages(['peer' => $chatID, 'id' => [$update["update"]["message"]["reply_to_msg_id"]]]);
    $reply_from_id = $gmsg['messages'][0]['from_id'];
    $myfile2 = fopen("enemy.txt", "a") or die("Unable to open file!");
    fwrite($myfile2, "$reply_from_id\n");
    fclose($myfile2);
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " Usᴇʀ : $reply_from_id
 Is Nᴏᴡ Iɴ Eɴᴇᴍʏ Lɪsᴛ", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
}
     }
     if ($msg == "setenemy") {
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $gmsg = $MadelineProto->channels->getMessages(['channel' => $chatID, 'id' => [$update["update"]["message"]["reply_to_msg_id"]]]);
    $reply_from_id = $gmsg['messages'][0]['from_id'];
    $myfile2 = fopen("enemy.txt", "a") or die("Unable to open file!");
    fwrite($myfile2, "$reply_from_id\n");
    fclose($myfile2);
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " Usᴇʀ : $reply_from_id
 Is Nᴏᴡ Iɴ Eɴᴇᴍʏ Lɪsᴛ", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
}
     }
     if (strpos($msg, "delenemy ") !== false) {
$prima2 = trim(str_replace("delenemy ", "", $msg));
$newlist = str_replace($prima2, "", $enemy);
file_put_contents("enemy.txt", $newlist);
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "ᴜsᴇʀ : $prima2
 ᴅᴇʟᴇᴛᴇ ᴇɴᴇᴍʏ ʟɪsᴛ
", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "delenemy") {
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $gmsg = $MadelineProto->messages->getMessages(['peer' => $chatID, 'id' => [$update["update"]["message"]["reply_to_msg_id"]]]);
    $reply_from_id = $gmsg['messages'][0]['from_id'];
    $newlist = str_replace($reply_from_id, "", $enemy);
    file_put_contents("enemy.txt", $newlist);
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " ᴜsᴇʀ : $reply_from_id
 ᴅᴇʟᴇᴛᴇ ᴇɴᴇᴍʏ ʟɪsᴛ", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
}
     }
     if ($msg == "delenemy") {
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $gmsg = $MadelineProto->channels->getMessages(['channel' => $chatID, 'id' => [$update["update"]["message"]["reply_to_msg_id"]]]);
    $reply_from_id = $gmsg['messages'][0]['from_id'];
    $newlist = str_replace($reply_from_id, "", $enemy);
    file_put_contents("enemy.txt", $newlist);
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " ᴜsᴇʀ : $reply_from_id
 ᴅᴇʟᴇᴛᴇ ᴇɴᴇᴍʏ ʟɪsᴛ", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
}
     }
     if ($msg == 'enemylist') {
$list = file_get_contents("$enemy.txt");
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "ᴇɴᴇᴍʏ Lɪsᴛ:

$enemy
", 'parse_mode' => 'MarkDown']);
     }
//---
     if ($msg == "enemy on") {
$Conf = json_decode(file_get_contents('Config.json'));
$Conf->Enemy = 1;
file_put_contents('Config.json', json_encode($Conf));
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' • sᴇʟғ ᴇɴᴇᴍʏ ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏɴ •', 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "enemy off") {
$Conf = json_decode(file_get_contents('Config.json'));
$Conf->Enemy = 0;
file_put_contents('Config.json', json_encode($Conf));
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => '• sᴇʟғ ᴇɴᴇᴍʏ  ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏғғ •', 'parse_mode' => 'MarkDown']);
     }
     if (strpos($msg, "ترجمه ") !== false) {
$word = trim(str_replace("ترجمه ", "", $msg));
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $gmsg = $MadelineProto->channels->getMessages(['channel' => $chatID, 'id' => [$update["update"]["message"]["reply_to_msg_id"]]]);
    $reply_to_msg_id = $update['update']['message']['reply_to_msg_id'];
    $messag1 = $gmsg['messages'][0]['message'];
    $messag = str_replace(" ", "+", $messag1);
    if ($word == "فارسی") {
        $url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=fa&text=$messag";
        $jsurl = json_decode(file_get_contents($url), true);
        $text9 = $jsurl['text'][0];
        $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => 'ᴛʀᴀɴsʟᴀᴛᴇ ғᴀ :

`' . $text9 . '`

', 'parse_mode' => 'MarkDown']);
    }
    if ($word == "انگلیسی") {
        $url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=en&text=$messag";
        $jsurl = json_decode(file_get_contents($url), true);
        $text9 = $jsurl['text'][0];
        $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' ᴛʀᴀɴsʟᴀᴛᴇ ᴇɴ :

`' . $text9 . '`

', 'parse_mode' => 'MarkDown']);
    }
    if ($word == "عربی") {
        $url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ar&text=$messag";
        $jsurl = json_decode(file_get_contents($url), true);
        $text9 = $jsurl['text'][0];
        $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' ᴛʀᴀɴsʟᴀᴛᴇ ᴀʀ :

`' . $text9 . '`
', 'parse_mode' => 'MarkDown']);
    }
}
     }
     if (strpos($msg, "translate ") !== false) {
$word = trim(str_replace("translate ", "", $msg));
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $gmsg = $MadelineProto->channels->getMessages(['channel' => $chatID, 'id' => [$update["update"]["message"]["reply_to_msg_id"]]]);
    $reply_to_msg_id = $update['update']['message']['reply_to_msg_id'];
    $messag1 = $gmsg['messages'][0]['message'];
    $messag = str_replace(" ", "+", $messag1);
    if ($word == "fa") {
        $url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=fa&text=$messag";
        $jsurl = json_decode(file_get_contents($url), true);
        $text9 = $jsurl['text'][0];
        $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' ᴛʀᴀɴsʟᴀᴛᴇ ғᴀ :

`' . $text9 . '`
', 'parse_mode' => 'MarkDown']);
    }
    if ($word == "en") {
        $url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=en&text=$messag";
        $jsurl = json_decode(file_get_contents($url), true);
        $text9 = $jsurl['text'][0];
        $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' ᴛʀᴀɴsʟᴀᴛᴇ ᴇɴ :

`' . $text9 . '`
', 'parse_mode' => 'MarkDown']);
    }
    if ($word == "ar") {
        $url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ar&text=$messag";
        $jsurl = json_decode(file_get_contents($url), true);
        $text9 = $jsurl['text'][0];
        $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' ᴛʀᴀɴsʟᴀᴛᴇ ᴀʀ :

`' . $text9 . '`
', 'parse_mode' => 'MarkDown']);
    }
}
     }

     if (preg_match("/^[\/\#\!]?(block) (.*)$/i", $msg)) {
preg_match("/^[\/\#\!]?(block) (.*)$/i", $msg, $text);
$MadelineProto->contacts->block(['id' => $text[2],]);
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "ᴜsᴇʀ :$text[2] ʙʟᴏᴄᴋᴇᴅ!", 'parse_mode' => 'MarkDown']);
     }
     if (preg_match("/^[\/\#\!]?(unblock) (.*)$/i", $msg)) {
preg_match("/^[\/\#\!]?(unblock) (.*)$/i", $msg, $text);
$MadelineProto->contacts->unblock(['id' => $text[2],]);
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "ᴜsᴇʀ :$text[2] ᴜɴʙʟᴏᴄᴋᴇᴅ!", 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "بن" || $msg == "مسدود" || $msg == "/ban" || $msg == "!ban" || $msg == "ban" || $msg == "اخراج") {
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $gmsg = $MadelineProto->channels->getMessages(['channel' => $chatID, 'id' => [$update["update"]["message"]["reply_to_msg_id"]]]);
    $reply_from_id = $gmsg['messages'][0]['from_id'];
    if ($reply_from_id !== false) {
        $channelBannedRights = ['_' => 'channelBannedRights', 'view_messages' => true, 'send_messages' => true, 'send_media' => true, 'send_stickers' => true, 'send_gifs' => true, 'send_games' => true, 'send_inline' => true, 'embed_links' => true, 'until_date' => 0];
        $MadelineProto->channels->editBanned(['channel' => $chatID, 'user_id' => $reply_from_id, 'banned_rights' => $channelBannedRights,]);
        $meee = $MadelineProto->get_full_info($reply_from_id);
        $meeee = $meee['User'];
        $first_name1 = $meeee['first_name'];
        $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " ʙᴀɴɴᴇᴅ", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
    }
}
     }
     if (preg_match("/^[\/\#\!]?(like) (.*)$/i", $msg)) {
preg_match("/^[\/\#\!]?(like) (.*)$/i", $msg, $text);
$txxxt = $text[2];
$messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@like", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
$query_id = $messages_BotResults['query_id'];
$query_res_id = $messages_BotResults['results'][0]['id'];
$MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
     }
     if ($msg == "حذف سنجاق" || $msg == "unpin" || $msg == "/unpin" || $msg == "!unpin") {
$MadelineProto->channels->updatePinnedMessage(['silent' => false, 'channel' => $chatID, 'id' => 0,]);
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "ᴜɴᴘɪɴɴᴇᴅ", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "سنجاق" || $msg == "pin" || $msg == "/pin" || $msg == "!pin") {
$repid = $update['update']['message']['reply_to_msg_id'];
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $type = $MadelineProto->get_info($chatID);
    $typ = $type['type'];
    $Updates = $MadelineProto->channels->updatePinnedMessage(['silent' => false, 'channel' => $chatID, 'id' => $repid,]);
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " ᴘɪɴɴᴇᴅ", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
}
     }
//
     if (preg_match("/^[\/\#\!]?(cleanenemylist)$/i", $msg)) {
unlink("enemy.txt");
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => 'ᴄʟᴇᴀɴ ᴇɴᴇᴍʏ ʟɪsᴛ', 'parse_mode' => 'MarkDown']);
     }
     if (strpos($msg, "setusername ") !== false) {
$ip = trim(str_replace("setusername ", "", $msg));
$ip = explode("|", $ip . "|||||");
$id = trim($ip[0]);
$User = $MadelineProto->account->updateUsername(['username' => "$id",]);
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' • **New Name Set** :
@' . $id . '️ ', 'parse_mode' => 'MarkDown']);
     }
     if (strpos($msg, "profile ") !== false) {
$ip = trim(str_replace("profile ", "", $msg));
$ip = explode("|", $ip . "|||||");
$id1 = trim($ip[0]);
$id2 = trim($ip[1]);
$id3 = trim($ip[2]);
$User = $MadelineProto->account->updateProfile(['first_name' => "$id1", 'last_name' => "$id2", 'about' => "$id3",]);
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "
 #ғɪʀsᴛ ɴᴀᴍᴇ ✅ : $id1

#ʟᴀsᴛ ɴᴀᴍᴇ ✅ : $id2

#ʙɪᴏ ✅ : $id3

️", 'parse_mode' => 'MarkDown']);
     }
     }
     if ((int)json_decode(file_get_contents('Config.json'))->Typing == 1) {
$sendMessageTypingAction = ['_' => 'sendMessageTypingAction'];
$m = $MadelineProto->messages->setTyping(['peer' => $chatID, 'action' => $sendMessageTypingAction]);
     }
     if ($userID == $admin) {
     if ($msg == "typing on" || $msg == "Typing on" || $msg == "Typing On") {
$Conf = json_decode(file_get_contents('Config.json'));

$Conf->Typing = 1;
file_put_contents('Config.json', json_encode($Conf));
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " sᴇʟғ ᴛʏᴘɪɴɢ ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏɴ •", 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "typing off" || $msg == "Typing Off" || $msg == "Typing off") {
$Conf = json_decode(file_get_contents('Config.json'));

$Conf->Typing = 0;
file_put_contents('Config.json', json_encode($Conf));
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " • sᴇʟғ ᴛʏᴘɪɴɢ ᴍᴏᴅᴇ ɪs ɴᴏᴡ ᴏғғ •", 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "number") {
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' ❶ ', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 1, 'message' => ' ❷ ', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 2, 'message' => ' ❸ ', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 3, 'message' => ' ❹', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 4, 'message' => '❺  ', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 5, 'message' => '❻  ', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 6, 'message' => ' ❼', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 7, 'message' => ' ❽ ', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 8, 'message' => ' ❾ ', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 9, 'message' => ' ➓ ', 'parse_mode' => 'MarkDown']);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id + 10, 'message' => ' پخخخ بای بای فرزندم شات شدی ', 'parse_mode' => 'MarkDown']);
$Updates = $MadelineProto->messages->sendScreenshotNotification(['peer' => $chatID, 'reply_to_msg_id' => $msg_id,]);
     }
     if (preg_match("/^[\/\#\!]?(time)$/i", $msg)) {
$messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "$usernamehelper", 'peer' => $chatID, 'query' => "time_", 'offset' => '0',]);
$query_id = $messages_BotResults['query_id'];
$query_res_id = $messages_BotResults['results'][0]['id'];
$MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
     }
     if (preg_match("/^[\/\#\!]?(ping)$/i", $msg)) {
$messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "$usernamehelper", 'peer' => $chatID, 'query' => "ping_", 'offset' => '0',]);
$query_id = $messages_BotResults['query_id'];
$query_res_id = $messages_BotResults['results'][0]['id'];
$MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
     }
     if (strpos($msg, "setanswer ") !== false) {
$ip = trim(str_replace("setanswer ", "", $msg));
$ip = explode("|", $ip . "|||||");
$txxt = trim($ip[0]);
$answeer = trim($ip[1]);
if (!isset($data['answering'][$txxt])) {
    $data['answering'][$txxt] = $answeer;

    file_put_contents("data.txt", json_encode($data));

    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " `$txxt` ➲ `$answeer` **Add To AnswerList** ️ ", 'parse_mode' => 'MarkDown']);
} else {
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " `$txxt` ➲ `$answeer` **Alerdy AnswerList ** ", 'parse_mode' => 'MarkDown']);
}
     }
     if (preg_match("/^[\/\#\!]?(answerlist)$/i", $msg)) {
if (count($data['answering']) > 0) {
    $txxxt = "Answer List:
";
    $counter = 1;
    foreach ($data['answering'] as $k => $ans) {
        $txxxt .= "$counter: $k => $ans \n";
        $counter++;
    }
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => $txxxt]);
} else {
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' **No Answer**
', 'parse_mode' => 'MarkDown']);
}
     }
     if (preg_match("/^[\/\#\!]?(delanswer) (.*)$/i", $msg)) {
preg_match("/^[\/\#\!]?(delanswer) (.*)$/i", $msg, $text);
$txxt = $text[2];
if (isset($data['answering'][$txxt])) {
    unset($data['answering'][$txxt]);
    file_put_contents("data.json", json_encode($data));
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "$txxt **Delete To Answer List** ️", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
} else {
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "$txxt **Not Found AnswerList** ️", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
}
     }
     if (preg_match("/^[\/\#\!]?(clean answers)$/i", $msg)) {
$data['answering'] = [];
file_put_contents("data.json", json_encode($data));
$ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => ' **لیست پاسخ خالی است!**️ ', 'parse_mode' => 'MarkDown']);
     }
     if ($msg == "سنجاق" || $msg == "pin" || $msg == "/pin" || $msg == "!pin") {
$repid = $update['update']['message']['reply_to_msg_id'];
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $type = $MadelineProto->get_info($chatID);
    $typ = $type['type'];
    $Updates = $MadelineProto->channels->updatePinnedMessage(['silent' => false, 'channel' => $chatID, 'id' => $repid,]);
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => " Pɪɴɴᴇᴅ", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
}
     }
     if ($msg == "id") {
$msgid = $update['update']['message']['reply_to_msg_id'];
$mah = $MadelineProto->messages->getMessages(['peer' => $chatID, 'id' => [$msgid]]);
$date = $mah['messages'][0]['date'];
$date = date('m/d/Y H:i:s', $date);
$message = $mah['messages'][0]['message'];
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $gmsg = $MadelineProto->messages->getMessages(['peer' => $chatID, 'id' => [$update["update"]["message"]["reply_to_msg_id"]]]);
    $reply_from_id = $gmsg['messages'][0]['from_id'];
    $meee = $MadelineProto->get_full_info($reply_from_id);
    $meeee = $meee['User'];
    $first_name1 = $meeee['first_name'];
    $usernam = $meeee['user_name'];
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "
➲ #ғ_ɴᴀᴍᴇ = $first_name1
➲ #ᴜsᴇʀ_Iᴅ = $reply_from_id
➲ ᴍᴇssᴀɢᴇ = $message
➲ ᴛɪᴍᴇ ᴍᴇssᴀɢᴇ = $date
️", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
}
     }
     if ($msg == "rem") {
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $msgid = $update['update']['message']['reply_to_msg_id'];
    $pv = $MadelineProto->messages->getHistory(['peer' => $chatID, 'offset_id' => 0, 'offset_date' => 0, 'add_offset' => 0, 'limit' => $msgid, 'max_id' => 0, 'min_id' => 0, 'hash' => 0]);
    foreach ($pv['messages'] as $message) {
        $MadelineProto->messages->deleteMessages([
   'revoke' => 'Bool',
   'peer' => $chatID,
   'id' => [$message['id']]
        ]);
    }
}
     }
     if ($msg == "id") {
$msgid = $update['update']['message']['reply_to_msg_id'];
$mah = $MadelineProto->channels->getMessages(['channel' => $chatID, 'id' => [$msgid]]);
$datee = $mah['messages'][0]['date'];
$datee = date('m/d/Y H:i:s', $datee);
$messages = $mah['messages'][0]['message'];
if (isset($update['update']['message']['reply_to_msg_id'])) {
    $gmsg = $MadelineProto->messages->getMessages(['peer' => $chatID, 'id' => [$update["update"]["message"]["reply_to_msg_id"]]]);
    $reply_from_id = $gmsg['messages'][0]['from_id'];
    $meee = $MadelineProto->get_full_info($reply_from_id);
    $meeee = $meee['User'];
    $first_name1 = $meeee['first_name'];
    $ed = $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "
 ➲ #ғ_ɴᴀᴍᴇ = $first_name1
➲ #ᴜsᴇʀ_Iᴅ = $reply_from_id
➲ ᴍᴇssᴀɢᴇ = $messages
➲ ᴛɪᴍᴇ ᴍᴇssᴀɢᴇ = $datee
", 'reply_to_msg_id' => $msg_id, 'parse_mode' => 'MarkDown']);
}
     }
}
 if (strpos($msg, "😐") !== false) {
     if ((int)json_decode(file_get_contents('Config.json'))->Poker == 1) {
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'message' => "😕", 'reply_to_msg_id' => $msg_id]);
     }
 }
 if ((int)json_decode(file_get_contents('Config.json'))->Enemy == 1) {
     if (stripos($enemy, "$userID") !== false) {
$MadelineProto->messages->deleteMessages([
    'revoke' => 'Bool',
    'peer' => $chatID,
    'id' => [$msg_id]
]);
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' =>
    $msg_id, 'message' =>
    $fosh, 'parse_mode' => 'MarkDown']);
     }
 }
 if (isset($data['answering'][$msg])) {
     $texx = $data['answering'][$msg];
     $MadelineProto->messages->sendMessage(['peer' => $chatID, 'message' => $texx, 'reply_to_msg_id' => $msg_id]);
 }
 if ((int)json_decode(file_get_contents('Config.json'))->Typing == 1) {

     $sendMessageTypingAction = ['_' => 'sendMessageTypingAction'];

     $m = $MadelineProto->messages->setTyping(['peer' => $chatID, 'action' => $sendMessageTypingAction]);

 }
 if ((int)json_decode(file_get_contents('Config.json'))->Markread == 1) {
     $msg_id = $update['update']['message']['id'];
     if ($chatID < 0) {
$msg_id = $update['update']['message']['id'];
$MadelineProto->channels->readHistory(['channel' => $chatID, 'max_id' => $msg_id]);
$MadelineProto->channels->readMessageContents(['channel' => $chatID, 'id' => [$msg_id]]);
     } else {
$MadelineProto->messages->readHistory(['peer' => $chatID, 'max_id' => $msg_id]);
     }
 }
      if ($userID == $admin) {
     if ($msg == 'ser' || $msg == 'سرور' || $msg == '!Condition' || $msg == '/Condition' || $msg == 'Condition') {
$load = sys_getloadavg();
$MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "sᴇʀᴠᴇʀ ᴘɪɴɢ : $load[0]", 'parse_mode' => 'markdown']);
     }

 if (preg_match("/^[\/\#\!]?(خروج|left)$/i", $msg)) {
     $type = $MadelineProto->get_info($chatID);
     $type3 = $type['type'];
     if ($type3 == "supergroup") {
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "Bye :>"]);
$MadelineProto->channels->leaveChannel(['channel' => $chatID,]);
     } else {
$MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "use this in SuperGroup X.X"]);
     }
 }
 if (preg_match("/^[\/\#\!]?(save)$/i", $msg) && isset($update['update']['message']['reply_to_msg_id'])) {
     $me = $MadelineProto->get_self();
     $me_id = $me['id'];
     $MadelineProto->messages->forwardMessages(['from_peer' => $chatID, 'to_peer' => $me_id, 'id' => [$update['update']['message']['reply_to_msg_id']],]);
     $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "sᴀᴠᴇᴅ"]);
 }
 if (preg_match("/^[\/\#\!]?(flood) ([0-9]+) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(flood) ([0-9]+) (.*)$/i", $msg, $text);
     $count = $text[2];
     $txt = $text[3];
     $spm = "";
     for ($i = 1; $i <= $count; $i++) {
$spm .= "$txt \n";
     }
     $MadelineProto->messages->sendMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => $spm]);
 }
 if (preg_match("/^[\/\#\!]?(spam) ([0-9]+) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(spam) ([0-9]+) (.*)$/i", $msg, $text);
     $count = $text[2];
     $txt = $text[3];
     for ($i = 1; $i <= $count; $i++) {
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'message' => $txt]);
     }
 }
 if (preg_match("/^[\/\#\!]?(info) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(info) (.*)$/i", $msg, $text);
     $mee = $MadelineProto->get_full_info($text[2]);
     $me = $mee['User'];
     $me_id = $me['id'];
     $me_status = $me['status']['_'];
     $me_bio = $mee['full']['about'];
     $me_common = $mee['full']['common_chats_count'];
     $me_name = $me['first_name'];
     $me_uname = $me['username'];
     $MadelineProto->messages->editMessage(['peer' => $chatID, 'id' => $msg_id, 'message' => "🎩<b>Name</b>: <a href='mention:$userID'>$me_name</a> \n<b>Username</b>: @$me_uname \n<b>User</b>??: $me_id \n<b>Status</b>🛂: $me_status \n<b>Bio</b>💭: $me_bio \n<b>Common Groups Count</b>👥: $me_common", 'parse_mode' => 'MarkDown']);
 }
 if (preg_match("/^[\/\#\!]?(blue) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(blue) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@TextMagicBot", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (strpos($msg, "hidden ") !== false) {
     $ip = trim(str_replace("/hidden ", "", $msg));
     $ip = explode("|", $ip . "|||||");
     $txxt = trim($ip[0]);
     $answeer = trim($ip[1]);
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@nnbbot", 'peer' => $chatID, 'query' => "$txxt $answeer", 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(short) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(short) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@ylinkpro_bot", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(apk) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(apk) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@apkdl_bot", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(calc) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(calc) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@MACLBot", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(sticker) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(sticker) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@big_text_bot", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(time) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(time) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@ClockBot", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(weather) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(weather) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@raindropsbot", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(joke)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(joke)$/i", $msg, $text);
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@function_robot", 'peer' => $chatID, 'query' => '', 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(google) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(google) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@GoogleDEBot", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][rand(0, count($messages_BotResults['results']))]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(gif) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(gif) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@gif", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][rand(0, count($messages_BotResults['results']))]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(pic) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(pic) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@pic", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][rand(0, count($messages_BotResults['results']))]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(voice) (.*)$/i", $msg)) {
     preg_match("/^[\/\#\!]?(voice) (.*)$/i", $msg, $text);
     $txxxt = $text[2];
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@melobot", 'peer' => $chatID, 'query' => $txxxt, 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][rand(0, count($messages_BotResults['results']))]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if (preg_match("/^[\/\#\!]?(panel)$/i", $msg)) {
     $messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => "@HelperSelf_Robot", 'peer' => $chatID, 'query' => "panel_", 'offset' => '0',]);
     $query_id = $messages_BotResults['query_id'];
     $query_res_id = $messages_BotResults['results'][0]['id'];
     $MadelineProto->messages->sendInlineBotResult(['silent' => true, 'background' => false, 'clear_draft' => true, 'peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'query_id' => $query_id, 'id' => "$query_res_id",]);
 }
 if ($msg == "delete account") {
     $MadelineProto->account->deleteAccount(['reason' => '@Source_Eliya',]);
 }
 if ($msg == 'stats') {
     $res = ['bot' => 0, 'user' => 0, 'chat' => 0, 'channel' => 0, 'supergroup' => 0];
     foreach ($MadelineProto->get_dialogs() as $dialog) {
$res[$MadelineProto->get_info($dialog)['type']]++;
     }
     $g = json_encode($res);
     $gf = json_decode($g);
     $users = $gf->user;
     $groups = $gf->chat;
     $supergroups = $gf->supergroup;
     $channels = $gf->channel;
     $bots = $gf->bot;
     $all = $users + $groups + $supergroups + $channels + $bots;
     $MadelineProto->messages->sendMessage([
'peer' => $chatID,
'message' => "
Stats Self:

ᴘᴠ ➲ $users
ɢʀᴏᴜᴘ ➲ $groups
sᴜᴘᴇʀɢʀᴏᴜᴘ ➲ $supergroups
ᴄʜᴀɴɴᴇʟ ➲ $channels
ʀᴏʙᴏᴛ ➲ $bots
ᴀʟʟ ➲ $all
"
     ]);

      }
      if ($msg == "/clean deleted" || $msg == "clean deleted" || $msg == "!clean deleted" || $msg == "پاکسازی دلت اکانت ها" || $msg == "حذف دلت اکانت ها") {
 $channelParticipantsRecent = ['_' => 'channelParticipantsRecent'];
 $channels_ChannelParticipants = $MadelineProto->channels->getParticipants(['channel' => $chatID, 'filter' => $channelParticipantsRecent, 'offset' => 0, 'limit' => 200, 'hash' => 0,]);
 $channelBannedRights = ['_' => 'channelBannedRights', 'view_messages' => true, 'send_messages' => false, 'send_media' => false, 'send_stickers' => false, 'send_gifs' => false, 'send_games' => false, 'send_inline' => false, 'embed_links' => false, 'until_date' => 0];
 $kl = $channels_ChannelParticipants['users'];
 $list = "";
 foreach ($kl as $key => $val) {
     $fon = $kl[$key]['deleted'];
     $fonid = $kl[$key]['id'];
     if ($fon == true) {
$list .= '' . $kl[$key]['id'] . "\n";
$MadelineProto->channels->editBanned([
    'channel' => $chatID,
    'user_id' => $fonid,
    'banned_rights' => $channelBannedRights]);
     }
 }
 $alaki = explode("\n", $list);
 $allcount = count($alaki) - 1;
 $MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'message' => "تعداد $allcount کاربر دیلیت اکانت از گروه شما پاک شد"]);
      }
      if ($msg == "/clean bots" || $msg == "clean bots" || $msg == "!clean bots" || $msg == "پاکسازی ربات ها" || $msg == "حذف ربات ها") {
 $channelParticipantsRecent = ['_' => 'channelParticipantsRecent'];
 $channels_ChannelParticipants = $MadelineProto->channels->getParticipants(['channel' => $chatID, 'filter' => $channelParticipantsRecent, 'offset' => 0, 'limit' => 200, 'hash' => 0,]);
 $channelBannedRights = ['_' => 'channelBannedRights', 'view_messages' => true, 'send_messages' => false, 'send_media' => false, 'send_stickers' => false, 'send_gifs' => false, 'send_games' => false, 'send_inline' => false, 'embed_links' => false, 'until_date' => 0];
 $kl = $channels_ChannelParticipants['users'];
 $list = "";
 foreach ($kl as $key => $val) {
     $fon = $kl[$key]['bot'];
     $fonid = $kl[$key]['id'];
     if ($fon == true) {
$list .= '' . $kl[$key]['id'] . "\n";
$MadelineProto->channels->editBanned([
    'channel' => $chatID,
    'user_id' => $fonid,
    'banned_rights' => $channelBannedRights]);
     }
 }
 $alaki = explode("\n", $list);
 $allcount = count($alaki) - 1;
 $MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id' => $msg_id, 'message' => "تعداد $allcount ربات از گروه شما پاک شد"]);
      }
      if ((int)json_decode(file_get_contents('Config.json'))->Online == 1) {
 $MadelineProto->account->updateStatus(['offline' => FALSE]);
      }
if(preg_match("/^[\/\#\!]?(info) (.*)$/i", $msg)){
preg_match("/^[\/\#\!]?(info) (.*)$/i", $msg, $text);
$mee = $MadelineProto->get_full_info($text[2]);
$me = $mee['User'];
$me_id = $me['id'];
$me_status = $me['status']['_'];
$me_bio = $mee['full']['about'];
$me_common = $mee['full']['common_chats_count'];
$me_name = $me['first_name'];
$me_uname = $me['username'];
$mes = "ID: $me_id \nName: $me_name \nUsername: @$me_uname \nStatus: $me_status \nBio: $me_bio \nCommon Groups Count: $me_common";
$MadelineProto->messages->editMessage(['peer' => $chatID, 'message' => $mes]);
}
//=======================================================
if ($msg == "فروارد به همه" || $msg == "forward to all"){
$idmsg=  $update['update']['message']['reply_to_msg_id'];
$dialogs = $MadelineProto->get_dialogs();
foreach ($dialogs as $peer) {
$type = $MadelineProto->get_info($peer);
$type3 = $type['type'];
if($type3 == "chat" || $type3 == "supergroup" || $type3 == "user"){
 $MadelineProto->messages->forwardMessages(['from_peer' => $chatID, 'to_peer' => $peer, 'id' => [$idmsg], ]);
}
}
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id'=>$msg_id ,'message' =>'↜ پیام شما با موفقیت فرواد شد シ']);
}
if(preg_match("/^(ارسال به همه) (.*)$/", $msg)){
preg_match("/^(ارسال به همه) (.*)$/", $msg, $msg2);
$text = $msg2[2];
$dialogs = $MadelineProto->get_dialogs();
foreach ($dialogs as $peer) {
$type = $MadelineProto->get_info($peer);
$type3 = $type['type'];
if($type3 == "supergroup" ||$type3 == "user"||$type3 == "chat"){
$MadelineProto->messages->sendMessage(['peer' => $peer, 'message' =>"$text"]);
}
}
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id'=>$msg_id , 'message' =>'↜ پیام شما با موفقیت ارسال شد シ','parse_mode' => "markdown"]);
}
	if(preg_match("/^(ارسال به پیوی ها) (.*)$/", $msg)){
preg_match("/^(ارسال به پیوی ها) (.*)$/", $msg, $msg2);
$text = $msg2[2];
$dialogs = $MadelineProto->get_dialogs();
foreach ($dialogs as $peer) {
$type = $MadelineProto->get_info($peer);
$type3 = $type['type'];
if($type3 == "user"){
$MadelineProto->messages->sendMessage(['peer' => $peer, 'message' =>"$text"]);
}
}
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id'=>$msg_id , 'message' =>'›› پیام شما به پیوی ها ارسال شد シ','parse_mode' => "markdown"]);
}

	if(preg_match("/^(ارسال به گروه ها) (.*)$/", $msg)){
preg_match("/^(ارسال به گروه ها) (.*)$/", $msg, $msg2);
$text = $msg2[2];
$dialogs = $MadelineProto->get_dialogs();
foreach ($dialogs as $peer) {
$type = $MadelineProto->get_info($peer);
$type3 = $type['type'];
if($type3 == "supergroup" || $type3 == "chat"){
$MadelineProto->messages->sendMessage(['peer' => $peer, 'message' =>"$text"]);
}
}
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id'=>$msg_id , 'message' =>'›› پیام شما به گروه ها ارسال شد シ','parse_mode' => "markdown"]);
	}
	if ($msg == "فروارد به پیوی ها" || $msg == "forward to pv"){
$idmsg=  $update['update']['message']['reply_to_msg_id'];
$dialogs = $MadelineProto->get_dialogs();
foreach ($dialogs as $peer) {
$type = $MadelineProto->get_info($peer);
$type3 = $type['type'];
if($type3 == "user"){
 $MadelineProto->messages->forwardMessages(['from_peer' => $chatID, 'to_peer' => $peer, 'id' => [$idmsg], ]);
}
}
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id'=>$msg_id ,'message' =>'↚ پیام شما به پیوی ها فروارد شد シ']);
}
if ($msg == "فروارد به گروه ها" || $msg == "forward to group"){
$idmsg=  $update['update']['message']['reply_to_msg_id'];
$dialogs = $MadelineProto->get_dialogs();
foreach ($dialogs as $peer) {
$type = $MadelineProto->get_info($peer);
$type3 = $type['type'];
if($type3 == "chat" || $type3 == "supergroup"){
 $MadelineProto->messages->forwardMessages(['from_peer' => $chatID, 'to_peer' => $peer, 'id' => [$idmsg], ]);
}
}
$MadelineProto->messages->sendMessage(['peer' => $chatID, 'reply_to_msg_id'=>$msg_id ,'message' =>'↚ پیام شما به گروه ها فروارد شد シ']);
}
  if ($msg == "delete account") {
     $MadelineProto->account->deleteAccount(['reason' => '@Source_Eliya',]);
     }
 }
 /*

📌 کانال ایلیا سورس
برای دریافت سورس های بیشتر به کانال ما سر بزنید :)
@Source_Eliya

*/
  ?>
  <?php
/*

📌 کانال ایلیا سورس
برای دریافت سورس های بیشتر به کانال ما سر بزنید :)
@Source_Eliya

*/
$fsh = rand(1,112);
switch ($fsh){
case 1:
echo "اوووووووف آبم ریخت رو ممه هات";
break;
case 2:
echo "کیرم تو ناموصت";
break;
case 3:
echo "کص ننت";
break;
case 4:
echo "‏کون میدی عشقم؟ 😍";
break;
case 5:
echo "ننه خیاری";
break;
case 6:
echo "پدر صگ";
break;
case 7:
echo "اوووف خارت زیرمه";
break;
case 8:
echo "کیرم لا پا ننت";
break;
case 9:
echo "فرزندم کیرم کوص مادرت";
break;
case 10:
echo "😂";
break;
case 11:
echo "‏ژان ژان چ کونی";
break;
case 12:
echo "مادر جنده";
break;
case 13:
echo "کیرم تو جد و آبادت";
break;
case 14:
echo "‏شاشیدم تو دهن ننت";
break;
case 15:
echo "‏کیر خـر";
break;
case 16:
echo "خواهرتو گاییدم فرزندم";
break;
case 17:
echo "ننه کص پریود";
break;
case 18:
echo "خار فراری";
break;
case 19:
echo "‏بگو از کص ننم خوردم شاخ شدم";
break;
case 20:
echo "کیری ناموس";
break;
case 21:
echo "چرا واسه بابات شاخ میشی؟";
break;
case 22:
echo "خار خشابی";
break;
case 23:
echo "دستم تو کون ننت";
break;
case 24:
echo "پرده ابجیت رو زدم";
break;
case 25:
echo "ناموس صلواتی";
break;
case 26:
echo "‏شل ناموس";
break;
case 27:
echo "خار کص هزاری";
 ‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌break;
case 28:
echo "‏درخت تو کص خارت";
break;
case "تایپم تو کون ننه جندت";
break;
case 30:
echo "ننه کص قلمبه";
break;
case 31:
echo "بگو ناموسم جندست";
break;
case 32:
echo "گوه خوردی شاخ شدی";
break;
case 33:
echo "‏میخوام حکایت ننتو بگم";
break;
case 34:
echo "مادر چصو فیل";
break;
case 35:
echo "حرومزاده";
break;
case 36:
echo "خارتم چیز خوبیه ها";
break;
case 37:
echo "‏:/کیرم هوس ننتو کرده";
break;
case 38:
echo "‏کونده کله کیری";
break;
case 39:
echo "ننه کاندوم دزد";
break;
case 40:
echo "ننه کیر دزد";
break;
case 41:
echo "ننه گشاد";
break;
case 42:
echo "کیرم تو اول و آخرت";
break;
case 43:
echo "‏کصکش اعظم";
break;
case 44:
echo "‏بابات و گاییدم";
break;
case 45:
echo "‏ننتو بدم گربه ها بکنن؟";
break;
case 46:
echo "ننه حشری";
break;
case 47:
echo "رفتم";
break;
case 48:
echo "‏ناموس برهنه";
break;
case 49:
echo "دستم تو شورت ننت";
break;
case 50:
echo "اینترنتم مثل ننت خرابه";
break;
case 51:
echo "خار کص پاره";
break;
case 52:
echo "کص نصلت با ص صابون";
break;
case 53:
echo "ننه فرغونی";
break;
case 54:
echo "نانوس ب خطا";
break;
case 55:
echo "تو کص خارت تلمبه بزنم؟";
break;
case 56:
echo "صیک ت کص خارت";
break;
case 57:
echo ":/مملکت تو کونت‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌";
break;
case 58:
echo "کص عمت";
break;
case 59:
echo "باعی بده پصر خوب";
break;
case 60:
echo "کص ننتو بمالم؟";
break;
case 61:
echo "کیرم تو استخونای بابات";
break;
case 62:
echo "پسرم برای هدایت شدن تو کص ننت ساخته شدیم =)";
break;
case 63:
echo "مادرتم خشاب منه";
break;
case 64:
echo "ببین کونی من تایپ میکنم تو سلف میاری😂";
break;
case 65:
echo "ببین کونی من تایپ میکنم تو خشاب میزنی";
break;
case 66:
echo "هر جور فک کنی مادرت زیرمه";
break;
case 67:
echo "مادر سفارشی";
break;
case 68:
echo "مادر فروشی";
break;
case 69:
echo "بخفت دیگه فرزندم";
break;
case 70:
echo "حرومزاده ای مثل تو از کیرم بالا میره";
break;
case 71:
echo "تو همونی نبودی کونی دادی تو کونت هم جای زخم بود اگه دروغ میگم عکس کونت بفرست";
break;
case 72:
echo "پفیوس";
break;
case 73:
echo "ننه سگی";
break;
case 74:
echo "ننتو واس یه سیگار میفروشی بدبخت";
break;
case 75:
echo "بیا بشین سرش تا باهات کاری نداشته باشم";
break;
case 78:
echo "ببین من اتحادیم اونم اتحاد عقرب که خانواده تو چیزی نیس ما نسلتونم گاییدیم ";
break;
case 79:
echo "😂";
break;
case 80:
echo "🖕🖕🖕🖕";
break;
case 81:
echo "🖕🖕🖕";
break;
case 82:
echo "🖕🖕";
break;
case 83:
echo "🖕";
break;
case 84:
echo "🖕🖕🖕🖕🖕";
break;
case 85:
echo "دارم با مادرت فکر میکنیم چجوری باهم سکس کنیم";
break;
case 86:
echo "مادرت مثل حوری بهشت هس";
break;
case 87:
echo "😡";
break;
case 88:
echo "دیگه از تخمم بالا نرو";
break;
case 89:
echo "بنال دیگه خفه شدی";
break;
case 90:
echo "ببین برو تا بگای سگ ندادمت";
break;
case 91:
echo "بیا بخورش ";
break;
case 92:
echo "اع فهمیدی بابات کیه اومدی بهش شاخ بشی";
break;
case 93:
echo "تخمی که من اون شب از قاشق از زمین ریختم تو کوصش تو بوجود اومدی";
break;
case 94:
echo "سگ جون با بابات درس بحرف";
break;
case 95:
echo "میدونی چیه وقتی من نیستم مادرت خود ادضایی میکنه";
break;
case 96:
echo "پسرم بسه";
break;
case 97:
echo "تخم منی تو😂😂";
break;
case 98:
echo "😂😂😂😂";
break;
case 99:
echo "😂😂😂";
break;
case 100:
echo "😂😂";
break;
case 101:
echo "😂";
break;
case 102:
echo "سگ جون";
break;
case 103:
echo "خار و مادرت گاییدم";
break;
case 104:
echo "تخم خر";
break;
case 105:
echo "کیرم تو روزی که به این دنیا پا گذاشتی";
break;
case 106:
echo "میدونی چیه تو عادت کردی مادرت بفروشی منم که فاحشه میخرم";
break;
case 108:
echo "مادرت بگا سگ رفت";
break;
case 109:
echo "بزار دیگه با مادرت میرم خونه بخوابم";
break;
case 110:
echo "دیوس کی بودی تو";
break;
case 111:
echo "بی غیرت کی بودی تو";
break;
case 112:
echo "پسر کی بودی تو";
break;
}
/*

📌 کانال ایلیا سورس
برای دریافت سورس های بیشتر به کانال ما سر بزنید :)
@Source_Eliya

*/
?>

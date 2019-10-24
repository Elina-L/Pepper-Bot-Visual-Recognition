<?xml version="1.0" encoding="UTF-8" ?>
<Package name="python-heavy-pepper" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="color" src="color/color.dlg" />
        <Dialog name="edb" src="edb/edb.dlg" />
        <Dialog name="pythonapplauncher" src="pythonapplauncher/pythonapplauncher.dlg" />
        <Dialog name="stop_dialog" src="stop_dialog/stop_dialog.dlg" />
        <Dialog name="ready_picture" src="ready_picture/ready_picture.dlg" />
        <Dialog name="play_more" src="play_more/play_more.dlg" />
        <Dialog name="is_correct" src="is_correct/is_correct.dlg" />
    </Dialogs>
    <Resources>
        <File name="index" src="html/index.html" />
        <File name="main" src="html/main.js" />
        <File name="main" src="main.py" />
        <File name="jquery.min" src="html/jquery.min.js" />
        <File name="Variable names" src="Variable names.txt" />
        <File name="index_zip" src="html/index_jokename.html" />
        <File name="index_jokenameOrig" src="html/index_jokenameOrig.html" />
        <File name="Blank" src="html/Blank.html" />
        <File name="Offer" src="html/Offer" />
        <File name="banane" src="banane.jpg" />
        <File name="rest_client" src="rest_client.py" />
    </Resources>
    <Topics>
        <Topic name="color_enu" src="color/color_enu.top" topicName="color" language="en_US" />
        <Topic name="edb_enu" src="edb/edb_enu.top" topicName="edb" language="en_US" />
        <Topic name="pythonapplauncher_enu" src="pythonapplauncher/pythonapplauncher_enu.top" topicName="pythonapplauncher" language="en_US" />
        <Topic name="stop_dialog_enu" src="stop_dialog/stop_dialog_enu.top" topicName="stop_dialog" language="en_US" />
        <Topic name="ready_picture_enu" src="ready_picture/ready_picture_enu.top" topicName="ready_picture" language="en_US" />
        <Topic name="play_more_enu" src="play_more/play_more_enu.top" topicName="" language="" />
        <Topic name="is_correct_enu" src="is_correct/is_correct_enu.top" topicName="is_correct" language="en_US" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>

import 'package:flutter/material.dart';
import 'package:marquee/marquee.dart';
import 'package:flet/flet.dart';

class MarqueeControl extends StatelessWidget {
  final Control? parent;
  final Control control;
  final FletControlBackend backend;

  const MarqueeControl({
    super.key, 
    required this.parent, 
    required this.control,
    required this.backend
    });

  @override
  Widget build(BuildContext context) {

    TextStyle? style;
    var styleNameOrData = control.attrString("style", null);
    if (styleNameOrData != null) {
        style = getTextStyle(context, styleNameOrData);
    }
    if (style == null && styleNameOrData != null) {
        try {
            style = parseTextStyle(Theme.of(context), control, "style");
        } on FormatException catch (_) {
            style = null;
        }
    }
    //   TextStyle? themeStyle;
    //   var styleName = control.attrString("theme_style", null);
    //   if (styleName != null) {
    //     themeStyle = getTextStyle(context, styleName);
    //   }

    //   if (style == null && themeStyle != null) {
    //     style = themeStyle;
    //   } else if (style != null && themeStyle != null) {
    //     style = themeStyle.merge(style);
    //   }


    bool onDone = control.attrBool("onDone", false)!;
    void onDone() {
        if (control.attrBool("onDone", false)!) {
            backend.triggerControlEvent(widget.control.id, "done");
        }
    }

    return constrainedControl(
      context,
      Marquee(
        text: control.attrString("text", ""),
        style: style,
        scrollAxis: control.parseAxis("scrollAxis", Axis.horizontal),
        crossAxisAlignment: parseCrossAxisAlignment(control.attrString("crossAxisAlignment"), CrossAxisAlignment.start)!,
        blankSpace: control.attrDouble("blankSpace", 0.0),
        velocity: control.attrDouble("velocity", 50.0),
        pauseAfterRound: Duration(milliseconds: control.attrInt("pauseAfterRound", 0)),
        startPadding: control.attrDouble("startPadding", 0.0),
        accelerationDuration: Duration(milliseconds: control.attrInt("accelerationDuration", 0)),
        accelerationCurve: parseCurve(control.attrString("accelerationCurve"), Curves.decelerate)!,
        decelerationDuration: Duration(milliseconds: control.attrInt("decelerationDuration", 0)),
        decelerationCurve: parseCurve(control.attrString("decelerationCurve"), Curves.decelerate)!,
        showFadingOnlyWhenScrolling: control.attrBool("showFadingOnlyWhenScrolling", true),
        numberOfRounds: control.attrInt("numberOfRounds")!,
        fadingEdgeStartFraction: control.attrDouble("fadingEdgeStartFraction", 0.0),
        fadingEdgeEndFraction: control.attrDouble("fadingEdgeEndFraction", 0.0),
        startAfter: Duration(milliseconds: control.attrInt("startAfter", 0)),
        textScaleFactor: control.attrDouble("textScaleFactor")!,
        textDirection: control.attrBool("rtl", true) ? TextDirection.rtl : TextDirection.ltr,
        onDone: onDone
      ),

      parent,
      control,
    );
  }
}

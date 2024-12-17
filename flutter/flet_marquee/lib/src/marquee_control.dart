import 'package:flutter/material.dart';
import 'package:marquee/marquee.dart';
import 'package:flet/flet.dart';

class MarqueeControl extends StatefulWidget {
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
  State<MarqueeControl> createState() => _MarqueeControlState();
}

class _MarqueeControlState extends State<MarqueeControl> with FletStoreMixin {
  @override
  Widget build(BuildContext context) {

    TextStyle? style;
    var styleNameOrData = widget.control.attrString("style", null);
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
    //   var styleName = widget.control.attrString("theme_style", null);
    //   if (styleName != null) {
    //     themeStyle = getTextStyle(context, styleName);
    //   }

    //   if (style == null && themeStyle != null) {
    //     style = themeStyle;
    //   } else if (style != null && themeStyle != null) {
    //     style = themeStyle.merge(style);
    //   }


    bool onDone = widget.control.attrBool("onDone", false)!;
    void onDone() {
        if (widget.control.attrBool("onDone", false)!) {
            widget.backend.triggerControlEvent(widget.control.id, "done");
        }
    }

    return constrainedControl(
      context,
      Marquee(
        text: widget.control.attrString("text", ""),
        style: style,
        scrollAxis: widget.control.parseAxis("scrollAxis", Axis.horizontal),
        crossAxisAlignment: parseCrossAxisAlignment(widget.control.attrString("crossAxisAlignment"), CrossAxisAlignment.start)!,
        blankSpace: widget.control.attrDouble("blankSpace", 0.0),
        velocity: widget.control.attrDouble("velocity", 50.0),
        pauseAfterRound: Duration(milliseconds: widget.control.attrInt("pauseAfterRound", 0)),
        startPadding: widget.control.attrDouble("startPadding", 0.0),
        accelerationDuration: Duration(milliseconds: widget.control.attrInt("accelerationDuration", 0)),
        accelerationCurve: parseCurve(widget.control.attrString("accelerationCurve"), Curves.decelerate)!,
        decelerationDuration: Duration(milliseconds: widget.control.attrInt("decelerationDuration", 0)),
        decelerationCurve: parseCurve(widget.control.attrString("decelerationCurve"), Curves.decelerate)!,
        showFadingOnlyWhenScrolling: widget.control.attrBool("showFadingOnlyWhenScrolling", true),
        numberOfRounds: widget.control.attrInt("numberOfRounds")!,
        fadingEdgeStartFraction: widget.control.attrDouble("fadingEdgeStartFraction", 0.0),
        fadingEdgeEndFraction: widget.control.attrDouble("fadingEdgeEndFraction", 0.0),
        startAfter: Duration(milliseconds: widget.control.attrInt("startAfter", 0)),
        textScaleFactor: widget.control.attrDouble("textScaleFactor")!,
        textDirection: widget.control.attrBool("rtl", true) ? TextDirection.rtl : TextDirection.ltr,
        onDone: onDone
      ),
      widget.parent,
      control
    );
  }
}
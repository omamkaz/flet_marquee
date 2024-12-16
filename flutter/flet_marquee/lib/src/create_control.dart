import 'package:flet/flet.dart';
import 'marquee_control.dart';


CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "marquee":
      return MarqueeControl(
            parent: args.parent, 
            control: args.control,
            backend: args.backend
        );
    default:
      return null;
  }
};

void ensureInitialized() {
  // Initialization if needed
}

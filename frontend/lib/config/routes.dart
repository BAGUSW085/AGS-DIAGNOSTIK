import 'package:flutter/material.dart';
import '../features/auth/screens/login_screen.dart';
import '../features/dashboard/screens/dashboard_screen.dart';
import '../features/diagnostic/screens/diagnostic_screen.dart';
import '../features/diagnostic/screens/diagnostic_result_screen.dart';
import '../features/manual/screens/manual_search_screen.dart';
import '../features/manual/screens/wiring_viewer_screen.dart';
import '../features/vehicle/screens/vehicle_list_screen.dart';
import '../features/vehicle/screens/vehicle_detail_screen.dart';
import '../features/work_order/screens/work_order_list_screen.dart';
import '../features/work_order/screens/work_order_form_screen.dart';
import '../features/inventory/screens/sparepart_list_screen.dart';
import '../features/inventory/screens/stock_movement_screen.dart';
import '../features/pos/screens/pos_screen.dart';
import '../features/pos/screens/invoice_screen.dart';

class AppRoutes {
  AppRoutes._();

  static const String login = '/login';
  static const String dashboard = '/dashboard';
  static const String diagnostic = '/diagnostic';
  static const String diagnosticResult = '/diagnostic/result';
  static const String manualSearch = '/manual/search';
  static const String wiringViewer = '/manual/wiring';
  static const String vehicleList = '/vehicles';
  static const String vehicleDetail = '/vehicles/detail';
  static const String workOrderList = '/work-orders';
  static const String workOrderForm = '/work-orders/form';
  static const String sparepartList = '/inventory';
  static const String stockMovement = '/inventory/movement';
  static const String pos = '/pos';
  static const String invoice = '/pos/invoice';

  static Map<String, WidgetBuilder> get routes {
    return {
      login: (context) => const LoginScreen(),
      dashboard: (context) => const DashboardScreen(),
      diagnostic: (context) => const DiagnosticScreen(),
      diagnosticResult: (context) => const DiagnosticResultScreen(),
      manualSearch: (context) => const ManualSearchScreen(),
      wiringViewer: (context) => const WiringViewerScreen(),
      vehicleList: (context) => const VehicleListScreen(),
      vehicleDetail: (context) => const VehicleDetailScreen(),
      workOrderList: (context) => const WorkOrderListScreen(),
      workOrderForm: (context) => const WorkOrderFormScreen(),
      sparepartList: (context) => const SparepartListScreen(),
      stockMovement: (context) => const StockMovementScreen(),
      pos: (context) => const PosScreen(),
      invoice: (context) => const InvoiceScreen(),
    };
  }
}

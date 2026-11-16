import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'config/app_theme.dart';
import 'config/routes.dart';
import 'features/auth/providers/auth_provider.dart';
import 'features/diagnostic/providers/diagnostic_provider.dart';
import 'features/manual/providers/manual_provider.dart';
import 'features/vehicle/providers/vehicle_provider.dart';
import 'features/work_order/providers/work_order_provider.dart';
import 'features/inventory/providers/inventory_provider.dart';
import 'features/pos/providers/pos_provider.dart';

class BengkelMasaDepanApp extends StatelessWidget {
  const BengkelMasaDepanApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthProvider()),
        ChangeNotifierProvider(create: (_) => DiagnosticProvider()),
        ChangeNotifierProvider(create: (_) => ManualProvider()),
        ChangeNotifierProvider(create: (_) => VehicleProvider()),
        ChangeNotifierProvider(create: (_) => WorkOrderProvider()),
        ChangeNotifierProvider(create: (_) => InventoryProvider()),
        ChangeNotifierProvider(create: (_) => PosProvider()),
      ],
      child: MaterialApp(
        title: 'AGOS SMART DIAGNOSTIK by Agos Corporation',
        debugShowCheckedModeBanner: false,
        theme: AppTheme.lightTheme,
        initialRoute: AppRoutes.login,
        routes: AppRoutes.routes,
      ),
    );
  }
}

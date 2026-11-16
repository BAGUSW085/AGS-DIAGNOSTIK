import 'package:flutter/material.dart';
import 'features/dashboard/presentation/screens/bengkel_dashboard_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  final provider = BengkelAppProvider(
    baseUrl: 'http://10.0.2.2:8000', // Gunakan http://localhost:8000 untuk Flutter Web/Desktop
  );
  runApp(BengkelMasaDepanApp(provider: provider));
}

class BengkelMasaDepanApp extends StatelessWidget {
  final BengkelAppProvider provider;

  const BengkelMasaDepanApp({super.key, required this.provider});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AGOS SMART DIAGNOSTIK by Agos Corporation',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF0F172A)),
        useMaterial3: true,
      ),
      home: BengkelDashboardScreen(provider: provider),
    );
  }
}

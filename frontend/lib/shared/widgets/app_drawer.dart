import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../config/app_theme.dart';
import '../../../config/routes.dart';
import '../../auth/providers/auth_provider.dart';

class AppDrawer extends StatelessWidget {
  const AppDrawer({super.key});

  @override
  Widget build(BuildContext context) {
    final auth = Provider.of<AuthProvider>(context);

    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: [
          DrawerHeader(
            decoration: const BoxDecoration(color: AppTheme.primaryColor),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                const CircleAvatar(
                  radius: 30,
                  backgroundColor: Colors.white24,
                  child: Icon(Icons.person, color: Colors.white, size: 36),
                ),
                const SizedBox(height: 12),
                Text(auth.userName, style: const TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold)),
                Text(auth.userRole.toUpperCase(), style: const TextStyle(color: AppTheme.secondaryLight, fontSize: 12)),
              ],
            ),
          ),
          _DrawerItem(icon: Icons.dashboard, title: 'Dashboard', route: AppRoutes.dashboard),
          _DrawerItem(icon: Icons.search, title: 'Smart Diagnostic', route: AppRoutes.diagnostic),
          _DrawerItem(icon: Icons.menu_book, title: 'Repair Manual & Wiring', route: AppRoutes.manualSearch),
          _DrawerItem(icon: Icons.assignment, title: 'Work Order (PKB)', route: AppRoutes.workOrderList),
          _DrawerItem(icon: Icons.directions_car, title: 'Data Kendaraan', route: AppRoutes.vehicleList),
          _DrawerItem(icon: Icons.inventory_2, title: 'Stok Sparepart', route: AppRoutes.sparepartList),
          _DrawerItem(icon: Icons.point_of_sale, title: 'Kasir (POS)', route: AppRoutes.pos),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.logout, color: AppTheme.errorColor),
            title: const Text('Logout', style: TextStyle(color: AppTheme.errorColor)),
            onTap: () async {
              await auth.logout();
              if (context.mounted) {
                Navigator.pushNamedAndRemoveUntil(context, AppRoutes.login, (route) => false);
              }
            },
          ),
        ],
      ),
    );
  }
}

class _DrawerItem extends StatelessWidget {
  final IconData icon;
  final String title;
  final String route;

  const _DrawerItem({required this.icon, required this.title, required this.route});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: Icon(icon, color: AppTheme.primaryColor),
      title: Text(title),
      onTap: () {
        Navigator.pop(context);
        Navigator.pushNamed(context, route);
      },
    );
  }
}


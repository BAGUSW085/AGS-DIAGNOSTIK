import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../config/app_theme.dart';
import '../../../config/routes.dart';
import '../../auth/providers/auth_provider.dart';
import '../../../shared/widgets/app_drawer.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final auth = Provider.of<AuthProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('AGOS SMART DIAGNOSTIK by Agos Corporation'),
        actions: [
          IconButton(
            icon: const Icon(Icons.notifications_outlined),
            onPressed: () {},
          ),
        ],
      ),
      drawer: const AppDrawer(),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Welcome Card
            Card(
              color: AppTheme.primaryColor,
              child: Padding(
                padding: const EdgeInsets.all(20),
                child: Row(
                  children: [
                    const CircleAvatar(
                      radius: 28,
                      backgroundColor: Colors.white24,
                      child: Icon(Icons.person, color: Colors.white, size: 32),
                    ),
                    const SizedBox(width: 16),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Selamat Datang,',
                            style: Theme.of(context).textTheme.bodyMedium?.copyWith(color: Colors.white70),
                          ),
                          Text(
                            auth.userName,
                            style: Theme.of(context).textTheme.titleLarge?.copyWith(
                                  color: Colors.white,
                                  fontWeight: FontWeight.bold,
                                ),
                          ),
                          Text(
                            auth.userRole.toUpperCase(),
                            style: Theme.of(context).textTheme.bodySmall?.copyWith(
                                  color: AppTheme.secondaryLight,
                                  fontWeight: FontWeight.w600,
                                ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 24),

            // Feature Title
            Text(
              'Menu Utama',
              style: Theme.of(context).textTheme.titleLarge,
            ),
            const SizedBox(height: 12),

            // Feature Grid
            GridView.count(
              crossAxisCount: 2,
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              mainAxisSpacing: 12,
              crossAxisSpacing: 12,
              childAspectRatio: 1.15,
              children: [
                _FeatureCard(
                  icon: Icons.search,
                  title: 'Smart\nDiagnostic',
                  subtitle: 'Diagnosa kerusakan',
                  color: const Color(0xFF1565C0),
                  onTap: () => Navigator.pushNamed(context, AppRoutes.diagnostic),
                ),
                _FeatureCard(
                  icon: Icons.menu_book,
                  title: 'Repair Manual\n& Wiring',
                  subtitle: 'Manual & DTC',
                  color: const Color(0xFF2E7D32),
                  onTap: () => Navigator.pushNamed(context, AppRoutes.manualSearch),
                ),
                _FeatureCard(
                  icon: Icons.assignment,
                  title: 'Work Order\n(PKB)',
                  subtitle: 'Kelola pengerjaan',
                  color: const Color(0xFFE65100),
                  onTap: () => Navigator.pushNamed(context, AppRoutes.workOrderList),
                ),
                _FeatureCard(
                  icon: Icons.directions_car,
                  title: 'Data\nKendaraan',
                  subtitle: 'Riwayat servis',
                  color: const Color(0xFF6A1B9A),
                  onTap: () => Navigator.pushNamed(context, AppRoutes.vehicleList),
                ),
                _FeatureCard(
                  icon: Icons.inventory_2,
                  title: 'Stok\nSparepart',
                  subtitle: 'Kelola gudang',
                  color: const Color(0xFF00838F),
                  onTap: () => Navigator.pushNamed(context, AppRoutes.sparepartList),
                ),
                _FeatureCard(
                  icon: Icons.point_of_sale,
                  title: 'Kasir\n(POS)',
                  subtitle: 'Transaksi & nota',
                  color: const Color(0xFFC62828),
                  onTap: () => Navigator.pushNamed(context, AppRoutes.pos),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class _FeatureCard extends StatelessWidget {
  final IconData icon;
  final String title;
  final String subtitle;
  final Color color;
  final VoidCallback onTap;

  const _FeatureCard({
    required this.icon,
    required this.title,
    required this.subtitle,
    required this.color,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 3,
      margin: EdgeInsets.zero,
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: color.withAlpha(25),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(icon, color: color, size: 28),
              ),
              const Spacer(),
              Text(
                title,
                style: Theme.of(context).textTheme.titleSmall?.copyWith(
                      fontWeight: FontWeight.w600,
                      height: 1.3,
                    ),
              ),
              const SizedBox(height: 2),
              Text(
                subtitle,
                style: Theme.of(context).textTheme.bodySmall,
              ),
            ],
          ),
        ),
      ),
    );
  }
}


class ApiConfig {
  ApiConfig._();

  static const String baseUrl = 'http://10.0.2.2:8000/api/v1';

  // Auth endpoints
  static const String auth = '/auth';
  static const String login = '/auth/login';
  static const String register = '/auth/register';
  static const String me = '/auth/me';

  // Vehicle endpoints
  static const String vehicles = '/vehicles';

  // Diagnostic endpoints
  static const String diagnostics = '/diagnostics';

  // Manual endpoints
  static const String manuals = '/manuals';

  // Work order endpoints
  static const String workOrders = '/work-orders';

  // Inventory endpoints
  static const String inventory = '/inventory';

  // Transaction / POS endpoints
  static const String transactions = '/transactions';

  // Customers
  static const String customers = '/customers';
}

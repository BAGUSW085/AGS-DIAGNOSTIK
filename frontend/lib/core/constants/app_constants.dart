class AppConstants {
  AppConstants._();

  static const String appName = 'AGOS SMART DIAGNOSTIK by Agos Corporation';
  static const String appTagline = 'AI-Powered Workshop Management';
  static const String appVersion = '1.0.0';

  // SharedPreferences keys
  static const String tokenKey = 'auth_token';
  static const String refreshTokenKey = 'refresh_token';
  static const String userKey = 'user_data';
  static const String isLoggedInKey = 'is_logged_in';

  // Pagination
  static const int defaultPageSize = 20;
  static const int maxPageSize = 100;

  // Timeouts
  static const int connectionTimeout = 30; // seconds
  static const int receiveTimeout = 30; // seconds

  // Date formats
  static const String dateFormat = 'dd/MM/yyyy';
  static const String dateTimeFormat = 'dd/MM/yyyy HH:mm';
  static const String apiDateFormat = 'yyyy-MM-dd';

  // Indonesian Rupiah
  static const String currencySymbol = 'Rp';
  static const String currencyLocale = 'id_ID';
}

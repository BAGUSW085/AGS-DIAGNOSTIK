import 'package:intl/intl.dart';

class Formatters {
  Formatters._();

  static final NumberFormat _currencyFormat = NumberFormat.currency(
    locale: 'id_ID',
    symbol: 'Rp ',
    decimalDigits: 0,
  );

  static final DateFormat _dateFormat = DateFormat('dd/MM/yyyy');
  static final DateFormat _dateTimeFormat = DateFormat('dd/MM/yyyy HH:mm');
  static final DateFormat _timeFormat = DateFormat('HH:mm');
  static final DateFormat _apiDateFormat = DateFormat('yyyy-MM-dd');

  /// Format a double amount to Indonesian Rupiah: Rp 1.000.000
  static String formatCurrency(double amount) {
    return _currencyFormat.format(amount);
  }

  /// Format a DateTime to dd/MM/yyyy
  static String formatDate(DateTime date) {
    return _dateFormat.format(date);
  }

  /// Format a DateTime to dd/MM/yyyy HH:mm
  static String formatDateTime(DateTime date) {
    return _dateTimeFormat.format(date);
  }

  /// Format a DateTime to HH:mm
  static String formatTime(DateTime date) {
    return _timeFormat.format(date);
  }

  /// Format a DateTime for API usage: yyyy-MM-dd
  static String formatApiDate(DateTime date) {
    return _apiDateFormat.format(date);
  }

  /// Parse an API date string (yyyy-MM-dd) to DateTime
  static DateTime? parseApiDate(String? dateStr) {
    if (dateStr == null || dateStr.isEmpty) return null;
    try {
      return _apiDateFormat.parse(dateStr);
    } catch (_) {
      return null;
    }
  }

  /// Format phone number for display
  static String formatPhone(String phone) {
    final cleaned = phone.replaceAll(RegExp(r'[^\d]'), '');
    if (cleaned.length <= 4) return cleaned;
    if (cleaned.length <= 8) {
      return '${cleaned.substring(0, 4)}-${cleaned.substring(4)}';
    }
    return '${cleaned.substring(0, 4)}-${cleaned.substring(4, 8)}-${cleaned.substring(8)}';
  }
}

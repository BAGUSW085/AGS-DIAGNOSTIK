class Validators {
  Validators._();

  /// Validates that a field is not empty
  static String? validateRequired(String? value, {String fieldName = 'Field'}) {
    if (value == null || value.trim().isEmpty) {
      return '$fieldName wajib diisi';
    }
    return null;
  }

  /// Validates an Indonesian phone number
  static String? validatePhone(String? value) {
    if (value == null || value.trim().isEmpty) {
      return 'Nomor telepon wajib diisi';
    }
    final cleaned = value.replaceAll(RegExp(r'[^\d+]'), '');
    // Indonesian phone: starts with 08, +62, or 62, followed by 8-13 digits
    final phoneRegex = RegExp(r'^(\+62|62|0)8[1-9][0-9]{6,11}$');
    if (!phoneRegex.hasMatch(cleaned)) {
      return 'Nomor telepon tidak valid (contoh: 08123456789)';
    }
    return null;
  }

  /// Validates an Indonesian vehicle plate number
  /// Format: 1-2 letters + 1-4 digits + 0-3 letters (e.g., B 1234 ABC, D 12 AB)
  static String? validatePlateNumber(String? value) {
    if (value == null || value.trim().isEmpty) {
      return 'Nomor plat wajib diisi';
    }
    final cleaned = value.replaceAll(RegExp(r'\s+'), '').toUpperCase();
    final plateRegex = RegExp(r'^[A-Z]{1,2}\d{1,4}[A-Z]{0,3}$');
    if (!plateRegex.hasMatch(cleaned)) {
      return 'Format plat tidak valid (contoh: B1234ABC)';
    }
    return null;
  }

  /// Validates email address format
  static String? validateEmail(String? value) {
    if (value == null || value.trim().isEmpty) {
      return 'Email wajib diisi';
    }
    final emailRegex = RegExp(
      r'^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,253}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,253}[a-zA-Z0-9])?)*$',
    );
    if (!emailRegex.hasMatch(value.trim())) {
      return 'Format email tidak valid';
    }
    return null;
  }

  /// Validates minimum length
  static String? validateMinLength(String? value, int minLength, {String fieldName = 'Field'}) {
    if (value == null || value.trim().isEmpty) {
      return '$fieldName wajib diisi';
    }
    if (value.trim().length < minLength) {
      return '$fieldName minimal $minLength karakter';
    }
    return null;
  }

  /// Validates that a numeric value is positive
  static String? validatePositiveNumber(String? value, {String fieldName = 'Nilai'}) {
    if (value == null || value.trim().isEmpty) {
      return '$fieldName wajib diisi';
    }
    final number = double.tryParse(value);
    if (number == null) {
      return '$fieldName harus berupa angka';
    }
    if (number <= 0) {
      return '$fieldName harus lebih dari 0';
    }
    return null;
  }
}

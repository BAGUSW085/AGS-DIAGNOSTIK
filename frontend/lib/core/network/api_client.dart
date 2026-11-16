import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../../config/api_config.dart';
import '../../core/constants/app_constants.dart';
import 'api_response.dart';

class ApiClient {
  static final ApiClient _instance = ApiClient._internal();
  factory ApiClient() => _instance;
  ApiClient._internal();

  final http.Client _client = http.Client();

  Future<Map<String, String>> _getHeaders({bool requiresAuth = true}) async {
    final headers = <String, String>{
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    };

    if (requiresAuth) {
      final prefs = await SharedPreferences.getInstance();
      final token = prefs.getString(AppConstants.tokenKey);
      if (token != null && token.isNotEmpty) {
        headers['Authorization'] = 'Bearer $token';
      }
    }

    return headers;
  }

  Uri _buildUri(String path, {Map<String, dynamic>? queryParams}) {
    final uri = Uri.parse('${ApiConfig.baseUrl}$path');
    if (queryParams != null && queryParams.isNotEmpty) {
      return uri.replace(queryParameters: queryParams.map(
        (key, value) => MapEntry(key, value.toString()),
      ));
    }
    return uri;
  }

  Future<ApiResponse<T>> get<T>(
    String path, {
    Map<String, dynamic>? queryParams,
    T Function(dynamic json)? fromJson,
    bool requiresAuth = true,
  }) async {
    try {
      final uri = _buildUri(path, queryParams: queryParams);
      final headers = await _getHeaders(requiresAuth: requiresAuth);
      final response = await _client
          .get(uri, headers: headers)
          .timeout(const Duration(seconds: AppConstants.connectionTimeout));

      return _handleResponse<T>(response, fromJson);
    } catch (e) {
      return ApiResponse.error('Connection error: ${e.toString()}');
    }
  }

  Future<ApiResponse<T>> post<T>(
    String path, {
    Map<String, dynamic>? body,
    T Function(dynamic json)? fromJson,
    bool requiresAuth = true,
  }) async {
    try {
      final uri = _buildUri(path);
      final headers = await _getHeaders(requiresAuth: requiresAuth);
      final response = await _client
          .post(uri, headers: headers, body: jsonEncode(body))
          .timeout(const Duration(seconds: AppConstants.connectionTimeout));

      return _handleResponse<T>(response, fromJson);
    } catch (e) {
      return ApiResponse.error('Connection error: ${e.toString()}');
    }
  }

  Future<ApiResponse<T>> put<T>(
    String path, {
    Map<String, dynamic>? body,
    T Function(dynamic json)? fromJson,
    bool requiresAuth = true,
  }) async {
    try {
      final uri = _buildUri(path);
      final headers = await _getHeaders(requiresAuth: requiresAuth);
      final response = await _client
          .put(uri, headers: headers, body: jsonEncode(body))
          .timeout(const Duration(seconds: AppConstants.connectionTimeout));

      return _handleResponse<T>(response, fromJson);
    } catch (e) {
      return ApiResponse.error('Connection error: ${e.toString()}');
    }
  }

  Future<ApiResponse<T>> delete<T>(
    String path, {
    T Function(dynamic json)? fromJson,
    bool requiresAuth = true,
  }) async {
    try {
      final uri = _buildUri(path);
      final headers = await _getHeaders(requiresAuth: requiresAuth);
      final response = await _client
          .delete(uri, headers: headers)
          .timeout(const Duration(seconds: AppConstants.connectionTimeout));

      return _handleResponse<T>(response, fromJson);
    } catch (e) {
      return ApiResponse.error('Connection error: ${e.toString()}');
    }
  }

  ApiResponse<T> _handleResponse<T>(
    http.Response response,
    T Function(dynamic json)? fromJson,
  ) {
    final statusCode = response.statusCode;
    dynamic responseBody;

    try {
      responseBody = jsonDecode(response.body);
    } catch (_) {
      responseBody = response.body;
    }

    if (statusCode >= 200 && statusCode < 300) {
      T? data;
      if (fromJson != null && responseBody != null) {
        data = fromJson(responseBody);
      } else if (responseBody is T) {
        data = responseBody;
      }
      return ApiResponse.success(
        data: data,
        message: responseBody is Map ? responseBody['message'] as String? : null,
      );
    } else if (statusCode == 401) {
      return ApiResponse.error('Sesi telah berakhir. Silakan login kembali.');
    } else if (statusCode == 403) {
      return ApiResponse.error('Anda tidak memiliki akses untuk fitur ini.');
    } else if (statusCode == 404) {
      return ApiResponse.error('Data tidak ditemukan.');
    } else if (statusCode == 422) {
      final errors = responseBody is Map ? responseBody['detail'] : null;
      return ApiResponse.error(
        'Validasi gagal.',
        errors: errors,
      );
    } else {
      final message = responseBody is Map
          ? (responseBody['message'] ?? responseBody['detail'] ?? 'Terjadi kesalahan pada server.')
          : 'Terjadi kesalahan pada server.';
      return ApiResponse.error(message.toString());
    }
  }

  Future<void> saveToken(String token) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(AppConstants.tokenKey, token);
  }

  Future<void> clearToken() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(AppConstants.tokenKey);
    await prefs.remove(AppConstants.userKey);
    await prefs.setBool(AppConstants.isLoggedInKey, false);
  }
}

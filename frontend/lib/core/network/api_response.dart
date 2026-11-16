class ApiResponse<T> {
  final bool isSuccess;
  final T? data;
  final String? message;
  final dynamic errors;

  const ApiResponse._({
    required this.isSuccess,
    this.data,
    this.message,
    this.errors,
  });

  factory ApiResponse.success({T? data, String? message}) {
    return ApiResponse._(
      isSuccess: true,
      data: data,
      message: message,
    );
  }

  factory ApiResponse.error(String message, {dynamic errors}) {
    return ApiResponse._(
      isSuccess: false,
      message: message,
      errors: errors,
    );
  }

  bool get isError => !isSuccess;

  bool get hasData => data != null;

  R when<R>({
    required R Function(T? data, String? message) success,
    required R Function(String message, dynamic errors) error,
  }) {
    if (isSuccess) {
      return success(data, message);
    } else {
      return error(message ?? 'Unknown error', errors);
    }
  }
}

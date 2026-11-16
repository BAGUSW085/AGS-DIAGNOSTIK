class Vehicle {
  final int? id;
  final int? customerId;
  final String plateNumber;
  final String brand;
  final String model;
  final int? year;
  final String? engineCode;
  final String? vin;
  final String? color;
  final int? mileage;
  final String? notes;
  final DateTime? createdAt;
  final DateTime? updatedAt;

  const Vehicle({
    this.id,
    this.customerId,
    required this.plateNumber,
    required this.brand,
    required this.model,
    this.year,
    this.engineCode,
    this.vin,
    this.color,
    this.mileage,
    this.notes,
    this.createdAt,
    this.updatedAt,
  });

  factory Vehicle.fromJson(Map<String, dynamic> json) {
    return Vehicle(
      id: json['id'] as int?,
      customerId: json['customer_id'] as int?,
      plateNumber: json['plate_number'] as String? ?? '',
      brand: json['brand'] as String? ?? '',
      model: json['model'] as String? ?? '',
      year: json['year'] as int?,
      engineCode: json['engine_code'] as String?,
      vin: json['vin'] as String?,
      color: json['color'] as String?,
      mileage: json['mileage'] as int?,
      notes: json['notes'] as String?,
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at'].toString())
          : null,
      updatedAt: json['updated_at'] != null
          ? DateTime.tryParse(json['updated_at'].toString())
          : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      if (id != null) 'id': id,
      if (customerId != null) 'customer_id': customerId,
      'plate_number': plateNumber,
      'brand': brand,
      'model': model,
      if (year != null) 'year': year,
      if (engineCode != null) 'engine_code': engineCode,
      if (vin != null) 'vin': vin,
      if (color != null) 'color': color,
      if (mileage != null) 'mileage': mileage,
      if (notes != null) 'notes': notes,
    };
  }

  String get displayName => '$brand $model ($plateNumber)';

  Vehicle copyWith({
    int? id,
    int? customerId,
    String? plateNumber,
    String? brand,
    String? model,
    int? year,
    String? engineCode,
    String? vin,
    String? color,
    int? mileage,
    String? notes,
    DateTime? createdAt,
    DateTime? updatedAt,
  }) {
    return Vehicle(
      id: id ?? this.id,
      customerId: customerId ?? this.customerId,
      plateNumber: plateNumber ?? this.plateNumber,
      brand: brand ?? this.brand,
      model: model ?? this.model,
      year: year ?? this.year,
      engineCode: engineCode ?? this.engineCode,
      vin: vin ?? this.vin,
      color: color ?? this.color,
      mileage: mileage ?? this.mileage,
      notes: notes ?? this.notes,
      createdAt: createdAt ?? this.createdAt,
      updatedAt: updatedAt ?? this.updatedAt,
    );
  }
}

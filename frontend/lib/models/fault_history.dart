class FaultHistory {
  final int? id;
  final int? vehicleId;
  final String? symptom;
  final String? diagnosis;
  final String? solution;
  final String? severity;
  final String? dtcCode;
  final double? confidence;
  final Map<String, dynamic>? aiResponse;
  final DateTime? diagnosedAt;
  final DateTime? createdAt;

  const FaultHistory({
    this.id,
    this.vehicleId,
    this.symptom,
    this.diagnosis,
    this.solution,
    this.severity,
    this.dtcCode,
    this.confidence,
    this.aiResponse,
    this.diagnosedAt,
    this.createdAt,
  });

  factory FaultHistory.fromJson(Map<String, dynamic> json) {
    return FaultHistory(
      id: json['id'] as int?,
      vehicleId: json['vehicle_id'] as int?,
      symptom: json['symptom'] as String?,
      diagnosis: json['diagnosis'] as String?,
      solution: json['solution'] as String?,
      severity: json['severity'] as String?,
      dtcCode: json['dtc_code'] as String?,
      confidence: (json['confidence'] as num?)?.toDouble(),
      aiResponse: json['ai_response'] as Map<String, dynamic>?,
      diagnosedAt: json['diagnosed_at'] != null
          ? DateTime.tryParse(json['diagnosed_at'].toString())
          : null,
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at'].toString())
          : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      if (id != null) 'id': id,
      if (vehicleId != null) 'vehicle_id': vehicleId,
      if (symptom != null) 'symptom': symptom,
      if (diagnosis != null) 'diagnosis': diagnosis,
      if (solution != null) 'solution': solution,
      if (severity != null) 'severity': severity,
      if (dtcCode != null) 'dtc_code': dtcCode,
      if (confidence != null) 'confidence': confidence,
      if (aiResponse != null) 'ai_response': aiResponse,
    };
  }

  String get severityLabel {
    switch (severity?.toLowerCase()) {
      case 'critical':
        return '🔴 Kritis';
      case 'high':
        return '🟠 Tinggi';
      case 'medium':
        return '🟡 Sedang';
      case 'low':
        return '🟢 Rendah';
      default:
        return '⚪ Tidak Diketahui';
    }
  }
}

import json
import random
import datetime
from typing import Dict, List, Tuple

class PhotoAestheticEvaluator:
    """AI摄影审美评估器"""
    
    def __init__(self):
        # 定义6个审美维度及其权重
        self.dimensions = {
            "光影": 0.20,      # 光线和阴影处理
            "色彩": 0.20,      # 色彩搭配和饱和度
            "构图": 0.25,      # 画面构图和布局
            "主题": 0.15,      # 主题表达清晰度
            "细节": 0.10,      # 细节处理质量
            "创意": 0.10       # 创意和独特性
        }
        
        # 模拟标注规则库
        self.rules = self._load_evaluation_rules()
        
    def _load_evaluation_rules(self) -> Dict:
        """加载评估规则"""
        return {
            "光影": ["曝光合理", "阴影自然", "高光不过曝", "光线方向一致"],
            "色彩": ["色调和谐", "饱和度适中", "无色彩断层", "白平衡准确"],
            "构图": ["主体突出", "视觉平衡", "遵循三分法", "留白适当"],
            "主题": ["主题明确", "情感传达", "故事性强", "视角独特"],
            "细节": ["纹理清晰", "噪点控制", "边缘锐利", "无瑕疵"],
            "创意": ["新颖独特", "突破常规", "艺术表达", "概念清晰"]
        }
    
    def evaluate_photo(self, photo_id: str, photo_metadata: Dict) -> Dict:
        """
        评估单张照片的审美质量
        
        Args:
            photo_id: 照片ID
            photo_metadata: 照片元数据
            
        Returns:
            评估结果字典
        """
        print(f"\n正在评估照片: {photo_id}")
        print(f"拍摄时间: {photo_metadata.get('timestamp', '未知')}")
        print(f"拍摄设备: {photo_metadata.get('device', '未知')}")
        
        scores = {}
        detailed_feedback = []
        
        # 对每个维度进行评分
        for dimension, weight in self.dimensions.items():
            # 模拟AI模型评分（实际项目中会调用真正的AI模型）
            base_score = random.uniform(6.0, 9.5)  # 基础分6-9.5
            
            # 根据规则符合度调整分数
            rule_compliance = self._check_rules_compliance(dimension, photo_metadata)
            adjusted_score = base_score * (0.7 + 0.3 * rule_compliance)
            
            scores[dimension] = round(adjusted_score, 1)
            
            # 生成详细反馈
            feedback = self._generate_feedback(dimension, adjusted_score, rule_compliance)
            detailed_feedback.append(feedback)
        
        # 计算总分（加权平均）
        total_score = sum(score * weight for score, weight in 
                         zip(scores.values(), self.dimensions.values()))
        total_score = round(total_score, 1)
        
        # 生成优化建议
        suggestions = self._generate_suggestions(scores)
        
        return {
            "photo_id": photo_id,
            "total_score": total_score,
            "dimension_scores": scores,
            "detailed_feedback": detailed_feedback,
            "optimization_suggestions": suggestions,
            "evaluation_time": datetime.datetime.now().isoformat()
        }
    
    def _check_rules_compliance(self, dimension: str, metadata: Dict) -> float:
        """检查规则符合度"""
        applicable_rules = self.rules.get(dimension, [])
        if not applicable_rules:
            return 0.8  # 默认符合度
        
        # 模拟规则检查（实际项目会使用CV算法）
        compliance_rate = random.uniform(0.7, 0.95)
        
        # 如果有EXIF信息，可以更精确评估
        if metadata.get("has_exif", False):
            compliance_rate = min(compliance_rate + 0.05, 1.0)
            
        return compliance_rate
    
    def _generate_feedback(self, dimension: str, score: float, compliance: float) -> Dict:
        """生成维度详细反馈"""
        if score >= 8.5:
            level = "优秀"
            comment = f"{dimension}表现非常出色，达到了专业水准"
        elif score >= 7.0:
            level = "良好"
            comment = f"{dimension}表现良好，有进一步提升空间"
        else:
            level = "待改进"
            comment = f"{dimension}需要重点改进"
        
        return {
            "dimension": dimension,
            "score": round(score, 1),
            "level": level,
            "compliance_rate": round(compliance * 100),
            "comment": comment
        }
    
    def _generate_suggestions(self, scores: Dict) -> List[str]:
        """生成优化建议"""
        suggestions = []
        
        # 找出分数最低的维度
        min_dimension = min(scores.items(), key=lambda x: x[1])
        
        if min_dimension[1] < 7.0:
            suggestions.append(f"建议重点改进{min_dimension[0]}，当前分数较低")
        
        # 通用建议
        suggestions.append("尝试调整拍摄角度和构图，寻找更佳视角")
        suggestions.append("注意光线条件，避免过曝或欠曝")
        suggestions.append("后期处理时保持色彩自然和谐")
        
        return suggestions
    
    def batch_evaluate(self, photo_list: List[Tuple[str, Dict]]) -> List[Dict]:
        """批量评估照片"""
        results = []
        print(f"开始批量评估 {len(photo_list)} 张照片...")
        
        for photo_id, metadata in photo_list:
            result = self.evaluate_photo(photo_id, metadata)
            results.append(result)
            
            # 打印简要结果
            print(f"照片 {photo_id} 总分: {result['total_score']}/10.0")
        
        return results

def main():
    """主函数"""
    print("=" * 50)
    print("AI摄影审美评估系统")
    print("=" * 50)
    
    # 初始化评估器
    evaluator = PhotoAestheticEvaluator()
    
    # 模拟照片数据
    sample_photos = [
        ("PORTRAIT_001", {
            "timestamp": "2024-01-15 14:30:00",
            "device": "Canon EOS R5",
            "category": "人像",
            "has_exif": True
        }),
        ("LANDSCAPE_001", {
            "timestamp": "2024-01-16 09:15:00",
            "device": "Sony A7III",
            "category": "风景",
            "has_exif": True
        }),
        ("STREET_001", {
            "timestamp": "2024-01-17 16:45:00",
            "device": "iPhone 15 Pro",
            "category": "街拍",
            "has_exif": False
        })
    ]
    
    # 批量评估
    results = evaluator.batch_evaluate(sample_photos)
    
    # 输出详细报告
    print("\n" + "=" * 50)
    print("评估报告摘要")
    print("=" * 50)
    
    for result in results:
        print(f"\n照片ID: {result['photo_id']}")
        print(f"综合评分: {result['total_score']}/10.0")
        print("维度评分:")
        for dim, score in result['dimension_scores'].items():
            print(f"  {dim}: {score}/10.0")
        
        print("优化建议:")
        for i, suggestion in enumerate(result['optimization_suggestions'][:2], 1):
            print(f"  {i}. {suggestion}")
    
    # 保存结果到JSON文件
    output_file = "evaluation_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n详细评估结果已保存至: {output_file}")
    print("评估完成！")

if __name__ == "__main__":
    main()
"""
Text processing utilities for resume and document analysis
"""
import re
from typing import List, Dict, Set
from collections import Counter


class TextProcessor:
    """Text processing utilities for resume analysis"""
    
    @staticmethod
    def extract_keywords(text: str, min_length: int = 3) -> List[str]:
        """Extract keywords from text"""
        # Remove special characters and split
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Filter by length and common stop words
        stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
            "of", "with", "by", "from", "as", "is", "was", "are", "were", "been",
            "be", "have", "has", "had", "do", "does", "did", "will", "would",
            "could", "should", "may", "might", "must", "can", "this", "that",
            "these", "those", "i", "you", "he", "she", "it", "we", "they"
        }
        
        keywords = [word for word in words if len(word) >= min_length and word not in stop_words]
        return keywords
    
    @staticmethod
    def extract_skills(text: str) -> List[str]:
        """Extract potential skills from text"""
        # Common skill patterns
        skill_patterns = [
            r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+(?:development|programming|engineering|analysis|design|management|administration)\b',
            r'\b(?:Python|Java|JavaScript|C\+\+|C#|SQL|HTML|CSS|React|Angular|Vue|Node\.js|Docker|Kubernetes|AWS|Azure|GCP)\b',
        ]
        
        skills = set()
        text_lower = text.lower()
        
        # Extract common technical skills
        common_skills = [
            "python", "java", "javascript", "sql", "html", "css", "react", "angular",
            "vue", "node.js", "docker", "kubernetes", "aws", "azure", "gcp",
            "machine learning", "deep learning", "data science", "agile", "scrum",
            "project management", "git", "linux", "rest api", "graphql", "mongodb",
            "postgresql", "mysql", "redis", "elasticsearch", "tensorflow", "pytorch",
            "pandas", "numpy", "scikit-learn", "tableau", "power bi", "excel",
        ]
        
        for skill in common_skills:
            if skill in text_lower:
                skills.add(skill.title())
        
        # Use regex patterns
        for pattern in skill_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            skills.update(matches)
        
        return sorted(list(skills))
    
    @staticmethod
    def calculate_keyword_match(text1: str, text2: str) -> Dict[str, Any]:
        """Calculate keyword matching between two texts"""
        keywords1 = set(TextProcessor.extract_keywords(text1))
        keywords2 = set(TextProcessor.extract_keywords(text2))
        
        common = keywords1.intersection(keywords2)
        unique_to_text1 = keywords1 - keywords2
        unique_to_text2 = keywords2 - keywords1
        
        match_score = len(common) / len(keywords2) * 100 if keywords2 else 0
        
        return {
            "match_score": round(match_score, 2),
            "common_keywords": sorted(list(common)),
            "missing_keywords": sorted(list(unique_to_text2)),
            "extra_keywords": sorted(list(unique_to_text1)),
            "total_keywords_text1": len(keywords1),
            "total_keywords_text2": len(keywords2),
        }
    
    @staticmethod
    def extract_sections(text: str) -> Dict[str, str]:
        """Extract sections from resume text"""
        sections = {}
        current_section = "header"
        current_content = []
        
        lines = text.split("\n")
        
        # Common section headers
        section_patterns = [
            r'^(?:experience|work experience|employment history)',
            r'^(?:education|academic background)',
            r'^(?:skills|technical skills|core competencies)',
            r'^(?:projects|project experience)',
            r'^(?:certifications|certificates)',
            r'^(?:summary|professional summary|objective)',
            r'^(?:achievements|accomplishments)',
        ]
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check if line is a section header
            is_section_header = False
            for pattern in section_patterns:
                if re.match(pattern, line, re.IGNORECASE):
                    # Save previous section
                    if current_content:
                        sections[current_section] = "\n".join(current_content)
                    
                    # Start new section
                    current_section = re.sub(r'[^a-z\s]', '', line.lower()).strip()
                    current_content = []
                    is_section_header = True
                    break
            
            if not is_section_header:
                current_content.append(line)
        
        # Save last section
        if current_content:
            sections[current_section] = "\n".join(current_content)
        
        return sections


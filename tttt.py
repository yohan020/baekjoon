import requests
import xml.etree.ElementTree as ET
import time
import json

# 국가법령정보센터 Open API 기본 설정
# 참고: 'test' 계정으로도 동작하지만, 정식 개발 시에는 법제처 사이트에서 무료 인증키를 발급받아야 합니다.
API_KEY = "yohanlee10" 
SEARCH_URL = "https://www.law.go.kr/DRF/lawSearch.do"
DETAIL_URL = "https://www.law.go.kr/DRF/lawService.do"

def get_precedent_list(query, display_count=5):
    """1단계: 특정 키워드로 판례 목록(일련번호)을 검색합니다."""
    params = {
        'OC': API_KEY,
        'target': 'prec', # 검색 대상: 판례
        'type': 'XML',
        'query': query,
        'display': display_count # 테스트를 위해 가져올 개수 제한
    }

    print(f"🔍 '{query}' 키워드로 판례 목록 검색 중...")
    response = requests.get(SEARCH_URL, params=params)

    if response.status_code != 200:
        print("API 호출에 실패했습니다.")
        return []

    # XML 응답 파싱
    root = ET.fromstring(response.text)
    prec_seqs = []

    # <prec> 태그 안의 <판례일련번호> 추출
    for prec in root.findall('.//prec'):
        seq = prec.findtext('판례일련번호')
        if seq:
            prec_seqs.append(seq)

    print(f"✅ 총 {len(prec_seqs)}개의 판례 일련번호를 찾았습니다.")
    return prec_seqs

def get_precedent_details(prec_seq):
    """2단계: 판례 일련번호로 상세 내용을 조회하고 핵심 데이터를 추출합니다."""
    params = {
        'OC': API_KEY,
        'target': 'prec',
        'type': 'XML',
        'ID': prec_seq
    }

    response = requests.get(DETAIL_URL, params=params)

    if response.status_code != 200:
        return None

    root = ET.fromstring(response.text)

    # 시뮬레이터 AI 학습에 필요한 핵심 데이터 파싱
    case_info = {
        '일련번호': prec_seq,
        '사건명': root.findtext('.//사건명', default='없음'),
        '사건종류명': root.findtext('.//사건종류명', default='없음'),
        # 판결요지: AI의 오답 리포트 논리 구성에 유용
        '판결요지': root.findtext('.//판결요지', default='없음').strip().replace('<br/>', '\n'),
        # 판례내용: 실제 범죄사실(사기 수법)이 포함된 전체 텍스트
        '판례내용': root.findtext('.//판례내용', default='없음').strip().replace('<br/>', '\n') 
    }

    return case_info

def main():
    search_keyword = "기망" # '전세사기', '기망' 등으로 변경 가능
    
    # 1. 판례 일련번호 가져오기 (빠른 테스트를 위해 3개만)
    seq_list = get_precedent_list(search_keyword, display_count=3)

    result_data = []

    # 2. 각 판례의 상세 정보 크롤링
    for seq in seq_list:
        print(f"📥 판례 상세 정보 조회 중... (일련번호: {seq})")
        details = get_precedent_details(seq)
        if details:
            result_data.append(details)

        # 공공 API 서버에 무리를 주지 않기 위한 1초 대기 (매너 타임)
        time.sleep(1)

    # 3. 결과 확인
    print("\n=== 🚀 크롤링 완료 ===")
    for data in result_data:
        print(f"📌 사건명: {data['사건명']}")
        print(f"📝 판결요지 (요약): {data['판결요지'][:150]}...") # 텍스트가 길어 150자만 출력
        print("-" * 50)
        
    # 4. JSON 파일로 저장 (Vector DB 연동 준비)
    with open('fraud_cases.json', 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=4)
    print("📁 'fraud_cases.json' 파일로 저장이 완료되었습니다.")

if __name__ == "__main__":
    main()
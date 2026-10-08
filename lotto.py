import random
import streamlit as st

# 세션 상태 초기화 (생성된 로또 번호 세트 목록 저장)
if "lotto_sets" not in st.session_state:
    st.session_state.lotto_sets = []


# 로또 공 색상 지정 함수 (번호 범위에 따른 색상 반환)
def get_ball_color(num):
    if num <= 10:
        return "#fbc400"  # 노란색
    elif num <= 20:
        return "#69c6f0"  # 파란색
    elif num <= 30:
        return "#ff7272"  # 빨간색
    elif num <= 40:
        return "#aaa"  # 회색
    else:
        return "#b0d840"  # 초록색


# 페이지 제목 설정
st.title("🎲 로또 번호 생성기")

# 로또 번호 생성 버튼 클릭 처리
if st.button("로또번호생성"):
    # 1~45 중복 없는 6개 번호 추출 및 정렬
    new_numbers = sorted(random.sample(range(1, 46), 6))

    # 최대 5개 세트만 유지 (최신 번호가 뒤에 추가되며, 5개 초과 시 가장 오래된 세트 삭제)
    if len(st.session_state.lotto_sets) >= 5:
        st.session_state.lotto_sets.pop(0)

    st.session_state.lotto_sets.append(new_numbers)

# 생성된 로또 번호 세트 목록 출력
if st.session_state.lotto_sets:
    st.subheader("생성된 로또 번호 목록")

    for idx, numbers in enumerate(st.session_state.lotto_sets, start=1):
        # 로또 공 스타일 HTML 생성
        balls_html = "".join([
            f'<span style="display:inline-block; width:40px; height:40px; line-height:40px; '
            f'border-radius:50%; background-color:{get_ball_color(n)}; color:white; '
            f'text-align:center; font-weight:bold; margin-right:8px;">{n}</span>'
            for n in numbers
        ])

        # 게임 번호와 공 출력
        st.markdown(f"**{idx}게임:** {balls_html}", unsafe_allow_html=True)
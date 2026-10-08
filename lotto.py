import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="로또 번호 생성기", page_icon="🎰")

st.title("🎰 행운의 로또 번호 생성기")

# 세션 상태 초기화 (생성된 로또 번호 세트 저장)
if 'lotto_sets' not in st.session_state:
    st.session_state.lotto_sets = []

# 실제 로또 공 색상 결정 함수
def get_ball_color(number):
    if number <= 10:
        return "#fbc400"  # 노랑
    elif number <= 20:
        return "#69c8f2"  # 파랑
    elif number <= 30:
        return "#ff7272"  # 빨강
    elif number <= 40:
        return "#aaaaaa"  # 회색
    else:
        return "#b0d840"  # 초록

# 로또 공 HTML/CSS 디자인
def create_ball_html(number):
    color = get_ball_color(number)
    return f"""
    <div style="
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background-color: {color};
        color: white;
        font-size: 20px;
        font-weight: bold;
        margin: 5px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    ">
        {number}
    </div>
    """

# 버튼 및 안내 메시지 배치
col1, col2 = st.columns([1, 3])
with col1:
    generate_btn = st.button("로또번호 생성", type="primary")
with col2:
    if len(st.session_state.lotto_sets) >= 5:
        st.warning("⚠️ 최대 5세트까지만 생성할 수 있습니다. 다시 시작하려면 초기화 버튼을 누르세요.")

# 버튼 클릭 시 동작 로직
if generate_btn:
    if len(st.session_state.lotto_sets) < 5:
        # 1~45 중 6개를 중복 없이 랜덤 추출 후 오름차순 정렬
        new_set = sorted(random.sample(range(1, 46), 6))
        st.session_state.lotto_sets.append(new_set)

# 생성된 번호 화면 출력
if st.session_state.lotto_sets:
    st.write("---")
    for i, lotto_set in enumerate(st.session_state.lotto_sets):
        st.write(f"**{i+1}번째 세트:**")
        html_str = "".join([create_ball_html(num) for num in lotto_set])
        st.markdown(html_str, unsafe_allow_html=True)
        st.write("") # 간격 띄우기

# 초기화 버튼
st.write("---")
if st.button("초기화 (다시 하기)"):
    st.session_state.lotto_sets = []
    st.rerun()
import streamlit as st

st.title("TÍNH TIỀN GỬI TIẾT KIỆM")

# Nhập dữ liệu
C = st.number_input("Nhập số tiền gửi (triệu đồng):", min_value=0.0)
i = st.number_input("Nhập lãi suất tiết kiệm theo năm (vd: 0.06):", min_value=0.0)
n = st.number_input("Nhập số tháng gửi:", min_value=0.0)

# Nút tính toán
if st.button("Tính toán"):

    # Lãi đơn
    A = C * (1 + i * n / 12)

    # Lãi kép
    B = C * (1 + i / 12) ** n

    st.subheader("Kết quả")
    st.write(f"**Tổng tiền nhận được theo lãi đơn:** {A:,.4f} triệu đồng")
    st.write(f"**Tổng tiền nhận được theo lãi kép:** {B:,.4f} triệu đồng")

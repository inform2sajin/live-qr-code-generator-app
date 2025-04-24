import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="🔗QR Code Generator", page_icon="🔳")

# Styles
st.markdown("""
<style>
.qr-title {
    font-size: 20px;
    font-weight: bold;
    color: #e63946;
    text-align: center;
    transition: all 0.80s ease-in-out;
    transform-origin: center;
    display: inline-block;
}
.qr-title::after,
.qr-title::before{
    content: '';
    position: absolute;
    width: 100%;
    height: 2px;
    background: linear-gradient(to right, #ff0000, #00ffff);
    bottom: -5px;
    left: 0;
    transform: scaleX(0);
    transform-origin: right;
    transition: transform 0.4s ease-out;
}
.qr-title::before {
    top: -5px;
    transform-origin: left;
}
.qr-title:hover::after,
.qr-title:hover::before {
    transform: scaleX(1);
}
</style>
<h1 class="qr-title"> 🌐 Your QR code generator 📷 🔗</h1>
""", unsafe_allow_html=True)
    
# Input from user
url = st.text_input("Paste your link here, and we’ll turn it into a QR code instantly:⚡")

if st.button("🔍 Generate QR code"):
    # Generate proper PIL image
    qr_image = qrcode.make(url).get_image()
    
    # Display QR code image
    st.image(qr_image, caption="🎉🎉🎉Your personalized QR code is here!🎉🎉🎉 ❤️ Sajin ❤️", use_container_width=True)
    
    # Prepare for download
    buf = io.BytesIO()
    qr_image.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    
    # Download button
    st.download_button("📥 Download QR Code", data=byte_im, file_name="qr_code.jpg", mime="image/jpeg")
    


import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# =========================================================
# CẤU HÌNH ỨNG DỤNG
# =========================================================
APP_NAME = "Career Compass_Quynh_"
APP_TITLE = "Khảo sát định hướng nghề nghiệp 30 câu"

st.set_page_config(
    page_title=f"{APP_TITLE} | {APP_NAME}",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# HÀM SVG
# =========================================================
def svg_to_data_uri(svg: str) -> str:
    return "data:image/svg+xml;charset=UTF-8," + urllib.parse.quote(svg)

def hero_svg():
    return svg_to_data_uri("""
    <svg width="1200" height="520" viewBox="0 0 1200 520" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#4F46E5"/>
          <stop offset="55%" stop-color="#7C3AED"/>
          <stop offset="100%" stop-color="#0F766E"/>
        </linearGradient>
        <filter id="s">
          <feDropShadow dx="0" dy="16" stdDeviation="18" flood-opacity=".18"/>
        </filter>
      </defs>
      <rect width="1200" height="520" rx="42" fill="url(#g)"/>
      <circle cx="1030" cy="90" r="90" fill="#fff" opacity=".08"/>
      <circle cx="110" cy="450" r="110" fill="#fff" opacity=".06"/>
      <circle cx="830" cy="410" r="65" fill="#fff" opacity=".05"/>

      <text x="74" y="118" fill="#EDE9FE" font-size="22" font-weight="700"
            font-family="Segoe UI, Arial, sans-serif">CAREER COMPASS_QUYNH_</text>
      <text x="74" y="190" fill="#FFFFFF" font-size="56" font-weight="800"
            font-family="Segoe UI, Arial, sans-serif">Khám phá hướng nghề</text>
      <text x="74" y="252" fill="#FFFFFF" font-size="56" font-weight="800"
            font-family="Segoe UI, Arial, sans-serif">phù hợp với bạn</text>
      <text x="74" y="312" fill="#EDE9FE" font-size="21"
            font-family="Segoe UI, Arial, sans-serif">30 câu hỏi • 6 nhóm RIASEC • Gợi ý ngành, nghề, kỹ năng và lộ trình</text>

      <rect x="755" y="74" width="350" height="362" rx="34" fill="#fff" filter="url(#s)"/>
      <circle cx="930" cy="150" r="62" fill="#EEF2FF"/>
      <path d="M900 153 L921 174 L964 126" fill="none" stroke="#5B5BD6" stroke-width="13"
            stroke-linecap="round" stroke-linejoin="round"/>
      <rect x="825" y="250" width="210" height="15" rx="7.5" fill="#D9DDF3"/>
      <rect x="825" y="286" width="165" height="15" rx="7.5" fill="#D9DDF3"/>
      <rect x="825" y="322" width="235" height="15" rx="7.5" fill="#D9DDF3"/>
      <rect x="825" y="358" width="145" height="15" rx="7.5" fill="#D9DDF3"/>
    </svg>
    """)

def illustration_svg(title, subtitle, accent="#5B5BD6", kind="compass"):
    if kind == "compass":
        graphic = """
        <circle cx="470" cy="190" r="92" fill="#F3F4FF"/>
        <circle cx="470" cy="190" r="58" fill="none" stroke="#5B5BD6" stroke-width="10"/>
        <path d="M470 132 L495 190 L470 248 L445 190 Z" fill="#7C3AED"/>
        <circle cx="470" cy="190" r="10" fill="#14B8A6"/>
        """
    elif kind == "quiz":
        graphic = """
        <rect x="385" y="90" width="180" height="230" rx="26" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="3"/>
        <circle cx="430" cy="145" r="16" fill="#EEF2FF"/>
        <path d="M422 145 l7 7 l12 -15" fill="none" stroke="#5B5BD6" stroke-width="5" stroke-linecap="round"/>
        <rect x="462" y="138" width="70" height="10" rx="5" fill="#D9DDF3"/>
        <circle cx="430" cy="200" r="16" fill="#ECFDF5"/>
        <path d="M422 200 l7 7 l12 -15" fill="none" stroke="#10B981" stroke-width="5" stroke-linecap="round"/>
        <rect x="462" y="193" width="82" height="10" rx="5" fill="#D9DDF3"/>
        <circle cx="430" cy="255" r="16" fill="#FFF7ED"/>
        <path d="M422 255 l7 7 l12 -15" fill="none" stroke="#F59E0B" stroke-width="5" stroke-linecap="round"/>
        <rect x="462" y="248" width="62" height="10" rx="5" fill="#D9DDF3"/>
        """
    else:
        graphic = """
        <rect x="380" y="112" width="210" height="190" rx="26" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="3"/>
        <rect x="420" y="245" width="26" height="28" rx="8" fill="#14B8A6"/>
        <rect x="462" y="205" width="26" height="68" rx="8" fill="#5B5BD6"/>
        <rect x="504" y="160" width="26" height="113" rx="8" fill="#7C3AED"/>
        <path d="M410 175 C450 135 505 130 552 142" fill="none" stroke="#F59E0B" stroke-width="8" stroke-linecap="round"/>
        """
    return svg_to_data_uri(f"""
    <svg width="700" height="360" viewBox="0 0 700 360" xmlns="http://www.w3.org/2000/svg">
      <rect width="700" height="360" rx="34" fill="#FFFFFF"/>
      <circle cx="610" cy="58" r="52" fill="{accent}" opacity=".08"/>
      <text x="56" y="105" fill="#172033" font-size="34" font-weight="800"
            font-family="Segoe UI, Arial, sans-serif">{title}</text>
      <text x="56" y="150" fill="#667085" font-size="18"
            font-family="Segoe UI, Arial, sans-serif">{subtitle}</text>
      <rect x="56" y="190" width="210" height="10" rx="5" fill="{accent}" opacity=".18"/>
      <rect x="56" y="220" width="168" height="10" rx="5" fill="{accent}" opacity=".12"/>
      {graphic}
    </svg>
    """)

def career_art(title, code, accent1, accent2):
    return svg_to_data_uri(f"""
    <svg width="760" height="420" viewBox="0 0 760 420" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="{accent1}"/>
          <stop offset="100%" stop-color="{accent2}"/>
        </linearGradient>
      </defs>
      <rect width="760" height="420" rx="34" fill="url(#g)"/>
      <circle cx="630" cy="86" r="68" fill="#fff" opacity=".10"/>
      <rect x="430" y="72" width="230" height="280" rx="30" fill="#fff" opacity=".97"/>
      <circle cx="545" cy="145" r="58" fill="#F5F5FF"/>
      <text x="545" y="166" text-anchor="middle" font-size="58" font-weight="800"
            fill="{accent1}" font-family="Segoe UI, Arial, sans-serif">{code}</text>
      <rect x="475" y="238" width="140" height="12" rx="6" fill="#D8DAED"/>
      <rect x="475" y="272" width="106" height="12" rx="6" fill="#D8DAED"/>
      <rect x="475" y="306" width="160" height="12" rx="6" fill="#D8DAED"/>
      <text x="64" y="145" fill="#FFFFFF" font-size="34" font-weight="800"
            font-family="Segoe UI, Arial, sans-serif">{title}</text>
      <text x="64" y="198" fill="#F5F3FF" font-size="18"
            font-family="Segoe UI, Arial, sans-serif">Hướng nghề nổi bật</text>
    </svg>
    """)

# =========================================================
# CSS - FONT TIẾNG VIỆT AN TOÀN
# =========================================================
st.markdown("""
<style>
:root{
    --bg:#F6F8FC;
    --card:#FFFFFF;
    --text:#172033;
    --muted:#667085;
    --line:#E7EAF2;
    --primary:#5B5BD6;
    --primary2:#7C3AED;
    --accent:#14B8A6;
    --soft:#EEF0FF;
    --shadow:0 12px 34px rgba(28,38,70,.08);
}
html, body, .stApp, [class*="css"], input, textarea, button, select{
    font-family: "Segoe UI", Tahoma, Arial, "Noto Sans", sans-serif !important;
}
.stApp{
    background:
      radial-gradient(circle at 8% 0%, rgba(91,91,214,.10), transparent 26%),
      radial-gradient(circle at 94% 5%, rgba(20,184,166,.08), transparent 23%),
      var(--bg);
    color:var(--text);
}
.block-container{
    max-width:1180px;
    padding-top:1.15rem;
    padding-bottom:3rem;
}
#MainMenu, footer, header{visibility:hidden;}
.hero-wrap{
    background:white;
    border:1px solid var(--line);
    border-radius:30px;
    padding:10px;
    box-shadow:var(--shadow);
    margin-bottom:26px;
}
.hero-wrap img{width:100%;border-radius:24px;display:block;}
.section-title{
    font-size:29px;
    font-weight:900;
    letter-spacing:-.5px;
    margin:12px 0 8px 0;
}
.section-sub{
    color:var(--muted);
    line-height:1.65;
    margin-bottom:18px;
}
.feature-card,.info-card,.result-card{
    background:rgba(255,255,255,.96);
    border:1px solid var(--line);
    border-radius:22px;
    padding:20px;
    box-shadow:var(--shadow);
    height:100%;
}
.feature-icon{
    width:46px;height:46px;border-radius:14px;
    display:flex;align-items:center;justify-content:center;
    background:var(--soft);font-size:24px;margin-bottom:12px;
}
.feature-title{font-size:17px;font-weight:850;margin-bottom:7px;}
.feature-desc,.muted{color:var(--muted);line-height:1.58;font-size:14px;}
.q-card{
    background:#fff;
    border:1px solid var(--line);
    border-radius:18px;
    padding:16px 18px 12px;
    margin:11px 0 8px;
    box-shadow:0 7px 20px rgba(30,41,59,.04);
}
.q-num{
    display:inline-flex;width:34px;height:34px;align-items:center;justify-content:center;
    background:var(--soft);color:#4338CA;border-radius:10px;font-weight:900;margin-right:10px;
}
.q-text{font-size:16px;font-weight:760;line-height:1.5;}
.metric-box{
    background:linear-gradient(180deg,#FFFFFF,#FAFAFF);
    border:1px solid var(--line);
    border-radius:20px;
    padding:18px;
    text-align:center;
    box-shadow:0 8px 22px rgba(30,41,59,.05);
}
.metric-val{font-size:34px;font-weight:950;color:#4338CA;line-height:1.1;}
.metric-label{color:var(--muted);font-size:13px;font-weight:750;margin-top:5px;}
.rank{font-size:12px;text-transform:uppercase;letter-spacing:.8px;font-weight:900;color:var(--primary);}
.result-title{font-size:22px;font-weight:900;margin:5px 0 8px;}
.result-desc{color:var(--muted);line-height:1.62;font-size:14px;}
.pill{
    display:inline-block;background:#F1F3FF;color:#4F46E5;
    padding:6px 10px;border-radius:999px;margin:4px 5px 0 0;
    font-size:12px;font-weight:800;
}
.notice{
    background:#FFF7ED;border:1px solid #FED7AA;color:#7C2D12;
    border-radius:16px;padding:15px 16px;line-height:1.6;
}
.roadmap{
    background:#FFFFFF;border:1px solid var(--line);
    border-radius:20px;padding:18px;box-shadow:0 8px 22px rgba(30,41,59,.04);
}
.roadmap b{color:#4338CA;}
div.stButton > button,
div[data-testid="stDownloadButton"] button{
    width:100%;border:none;border-radius:14px;padding:.88rem 1.1rem;
    font-weight:850;background:linear-gradient(135deg,#4F46E5,#7C3AED);
    color:white;box-shadow:0 10px 24px rgba(79,70,229,.20);
}
div.stButton > button:hover,
div[data-testid="stDownloadButton"] button:hover{
    color:white;border:none;transform:translateY(-1px);
}
.stProgress > div > div > div > div{
    background:linear-gradient(90deg,#5B5BD6,#14B8A6);
}
@media(max-width:768px){.section-title{font-size:24px;}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# DỮ LIỆU
# =========================================================
questions = [
    ("R","Tôi thích sửa chữa, lắp ráp hoặc thao tác với máy móc, thiết bị."),
    ("I","Tôi thích tìm hiểu nguyên nhân của một vấn đề và phân tích dữ liệu để tìm câu trả lời."),
    ("A","Tôi thích sáng tạo hình ảnh, nội dung, âm nhạc hoặc những ý tưởng mới."),
    ("S","Tôi cảm thấy hứng thú khi hướng dẫn, hỗ trợ hoặc giúp người khác tiến bộ."),
    ("E","Tôi thích thuyết phục, đàm phán hoặc dẫn dắt người khác cùng đạt mục tiêu."),
    ("C","Tôi thích sắp xếp thông tin, hồ sơ, kế hoạch và làm việc theo quy trình rõ ràng."),
    ("R","Tôi thích những công việc tạo ra kết quả cụ thể bằng tay hoặc công cụ."),
    ("I","Tôi có hứng thú với nghiên cứu, công nghệ, khoa học hoặc giải quyết bài toán khó."),
    ("A","Tôi thường nghĩ ra nhiều cách thể hiện khác nhau cho cùng một ý tưởng."),
    ("S","Tôi thích lắng nghe và đưa ra lời khuyên khi người khác gặp khó khăn."),
    ("E","Tôi muốn thử sức trong kinh doanh, bán hàng hoặc phát triển dự án."),
    ("C","Tôi cảm thấy thoải mái khi làm việc với số liệu, biểu mẫu và lịch trình."),
    ("R","Tôi thích di chuyển, thao tác thực tế hơn là ngồi bàn làm việc suốt ngày."),
    ("I","Tôi thích kiểm chứng thông tin thay vì chỉ chấp nhận câu trả lời có sẵn."),
    ("A","Tôi quan tâm tới thiết kế, truyền thông, nghệ thuật hoặc cách kể chuyện hấp dẫn."),
    ("S","Tôi muốn công việc của mình tạo ra tác động tích cực trực tiếp cho con người."),
    ("E","Tôi thấy hứng thú với việc trình bày ý tưởng trước nhóm hoặc khách hàng."),
    ("C","Tôi chú ý chi tiết và thường phát hiện lỗi nhỏ trong tài liệu hoặc dữ liệu."),
    ("R","Tôi thích học qua thực hành, thử nghiệm trực tiếp và quan sát kết quả."),
    ("I","Tôi có thể kiên trì với một vấn đề trong thời gian dài để tìm ra lời giải hợp lý."),
    ("A","Tôi thích môi trường cho phép thử nghiệm phong cách và cách làm mới."),
    ("S","Tôi hợp với môi trường làm việc có nhiều tương tác và hợp tác giữa mọi người."),
    ("E","Tôi thích đặt mục tiêu, theo dõi kết quả và tạo ảnh hưởng tới quyết định của nhóm."),
    ("C","Tôi thích lập kế hoạch trước và cảm thấy hiệu quả hơn khi có hệ thống rõ ràng."),
    ("R","Tôi hứng thú với kỹ thuật, vận hành, sản xuất, xây dựng hoặc các công việc hiện trường."),
    ("I","Tôi muốn hiểu sâu cách một hệ thống hoạt động và tìm cách tối ưu nó."),
    ("A","Tôi thích viết, quay dựng, thiết kế hoặc phát triển trải nghiệm cho người dùng."),
    ("S","Tôi thích đào tạo, chăm sóc khách hàng, tư vấn hoặc làm việc cộng đồng."),
    ("E","Tôi tự tin khi thương lượng, kết nối quan hệ hoặc trình bày giá trị của một sản phẩm."),
    ("C","Tôi thích kiểm soát tiến độ, ngân sách, chứng từ hoặc các đầu việc cần độ chính xác."),
]

labels = {
    "R":"Thực tế – Kỹ thuật",
    "I":"Nghiên cứu – Phân tích",
    "A":"Sáng tạo – Nghệ thuật",
    "S":"Xã hội – Hỗ trợ",
    "E":"Quản lý – Kinh doanh",
    "C":"Tổ chức – Quy trình",
}

career_map = {
    "R":{
        "title":"Kỹ thuật – Công nghệ ứng dụng",
        "desc":"Phù hợp với người thích thao tác thực tế, máy móc, công cụ, hiện trường và kết quả hữu hình.",
        "majors":["Cơ khí","Điện – điện tử","Ô tô","Xây dựng","Công nghệ kỹ thuật"],
        "jobs":["Kỹ sư cơ khí","Kỹ thuật điện","Kỹ thuật ô tô","Kỹ sư công trình","Kỹ sư vận hành"],
        "skills":["Tư duy kỹ thuật","Đọc bản vẽ","An toàn lao động","Giải quyết sự cố"],
        "subjects":["Toán","Vật lý","Công nghệ","Tin học"],
        "environment":"Môi trường thực hành, phòng lab, xưởng, công trường hoặc bộ phận vận hành.",
        "c1":"#0F766E","c2":"#14B8A6"
    },
    "I":{
        "title":"Công nghệ – Dữ liệu – Nghiên cứu",
        "desc":"Phù hợp với người thích phân tích, tìm nguyên nhân, nghiên cứu hệ thống và xử lý vấn đề phức tạp.",
        "majors":["Công nghệ thông tin","Khoa học dữ liệu","AI","Phân tích kinh doanh","Nghiên cứu thị trường"],
        "jobs":["Data Analyst","Lập trình viên","AI/ML Engineer","Business Analyst","R&D"],
        "skills":["Logic","Python/SQL","Nghiên cứu","Tư duy hệ thống","Phân tích dữ liệu"],
        "subjects":["Toán","Tin học","Thống kê","Tiếng Anh"],
        "environment":"Môi trường phân tích, nghiên cứu, công nghệ, dữ liệu và các dự án cần chiều sâu.",
        "c1":"#2563EB","c2":"#06B6D4"
    },
    "A":{
        "title":"Sáng tạo – Truyền thông – Thiết kế",
        "desc":"Phù hợp với người thích tạo ý tưởng, kể chuyện, thiết kế, nội dung và trải nghiệm mới.",
        "majors":["Marketing","Truyền thông","Thiết kế đồ họa","UI/UX","Sản xuất nội dung"],
        "jobs":["Content Marketing","Graphic Designer","UI/UX Designer","Video Creator","Brand Planner"],
        "skills":["Storytelling","Thiết kế","Viết nội dung","Visual thinking","Sáng tạo ý tưởng"],
        "subjects":["Ngữ văn","Mỹ thuật","Tin học","Tiếng Anh"],
        "environment":"Môi trường linh hoạt, giàu ý tưởng, truyền thông, agency, studio hoặc đội sản phẩm.",
        "c1":"#7C3AED","c2":"#EC4899"
    },
    "S":{
        "title":"Giáo dục – Tư vấn – Dịch vụ con người",
        "desc":"Phù hợp với người có động lực hỗ trợ, hướng dẫn và tạo giá trị trực tiếp cho người khác.",
        "majors":["Giáo dục","Tâm lý học","Nhân sự","Công tác xã hội","Dịch vụ khách hàng"],
        "jobs":["Giáo viên","HR","Tư vấn viên","Customer Success","Chuyên viên đào tạo"],
        "skills":["Giao tiếp","Lắng nghe","Thuyết trình","Huấn luyện","Giải quyết xung đột"],
        "subjects":["Ngữ văn","Sinh học","GDCD","Tiếng Anh"],
        "environment":"Môi trường có nhiều tương tác, cộng đồng, giáo dục, dịch vụ và chăm sóc con người.",
        "c1":"#059669","c2":"#84CC16"
    },
    "E":{
        "title":"Kinh doanh – Marketing – Quản lý",
        "desc":"Phù hợp với người thích ảnh hưởng, phát triển cơ hội, dẫn dắt mục tiêu và làm việc với thị trường.",
        "majors":["Quản trị kinh doanh","Marketing","Thương mại điện tử","Kinh doanh quốc tế","Quản trị dự án"],
        "jobs":["Marketing Executive","Sales","Business Development","Project Manager","Account Manager"],
        "skills":["Đàm phán","Thuyết phục","Lãnh đạo","Tư duy kinh doanh","Quản trị mục tiêu"],
        "subjects":["Toán","Ngữ văn","Tiếng Anh","Tin học"],
        "environment":"Môi trường năng động, hướng mục tiêu, khách hàng, thị trường và phát triển kinh doanh.",
        "c1":"#EA580C","c2":"#F59E0B"
    },
    "C":{
        "title":"Tài chính – Vận hành – Hệ thống",
        "desc":"Phù hợp với người coi trọng độ chính xác, tổ chức, dữ liệu, quy trình và tính ổn định.",
        "majors":["Kế toán","Tài chính – Ngân hàng","Kiểm toán","Logistics","Quản trị vận hành"],
        "jobs":["Kế toán viên","Financial Analyst","Kiểm toán viên","Operations Executive","Supply Chain Planner"],
        "skills":["Excel","Quản lý dữ liệu","Kiểm soát quy trình","Lập kế hoạch","Độ chính xác"],
        "subjects":["Toán","Tin học","Kinh tế","Tiếng Anh"],
        "environment":"Môi trường có quy trình rõ ràng, dữ liệu, tài chính, vận hành hoặc kiểm soát nội bộ.",
        "c1":"#475569","c2":"#64748B"
    },
}

combo_suggestions = {
    "AI":("Thiết kế sản phẩm số – UX Research",["UX Researcher","Product Designer","Creative Technologist"]),
    "AE":("Marketing sáng tạo – Thương hiệu",["Brand Marketing","Creative Planner","Social Media Strategist"]),
    "AS":("Truyền thông – Giáo dục sáng tạo",["Content Educator","Instructional Designer","Community Content"]),
    "EI":("Chiến lược – Phân tích kinh doanh",["Business Analyst","Growth Analyst","Product Manager"]),
    "EC":("Quản trị – Tài chính – Vận hành",["Operations Manager","Account Manager","Commercial Finance"]),
    "ES":("Kinh doanh dịch vụ – Phát triển khách hàng",["Consultant","Customer Success","HR Business Partner"]),
    "IC":("Dữ liệu – Tài chính – Kiểm soát",["Data Analyst","Risk Analyst","Financial Analyst"]),
    "IR":("Kỹ thuật – Công nghệ – R&D",["Software Engineer","Automation Engineer","R&D Engineer"]),
    "RC":("Vận hành – Kỹ thuật – Chất lượng",["QA/QC","Supply Chain","Production Planner"]),
    "RS":("Dịch vụ kỹ thuật – Hỗ trợ ứng dụng",["Kỹ thuật viên","Kỹ sư dịch vụ","Technical Support"]),
    "CS":("Hành chính – Dịch vụ – Nhân sự",["HR Operations","Academic Coordinator","Customer Operations"]),
}

scale_text = {
    1:"1 · Hoàn toàn không đúng",
    2:"2 · Ít đúng",
    3:"3 · Phân vân",
    4:"4 · Khá đúng",
    5:"5 · Rất đúng",
}

# =========================================================
# HERO + GIỚI THIỆU
# =========================================================
st.markdown(f'<div class="hero-wrap"><img src="{hero_svg()}"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Bạn sẽ nhận được gì?</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Không chỉ là điểm số. Ứng dụng sẽ giúp bạn nhìn ra nhóm nghề nổi bật, môi trường phù hợp, kỹ năng nên phát triển và lộ trình thử nghiệm thực tế.</div>', unsafe_allow_html=True)

f1,f2,f3,f4 = st.columns(4)
features = [
    ("🧠","30 câu hỏi","Khảo sát sở thích, cách làm việc và môi trường khiến bạn cảm thấy thoải mái."),
    ("🧭","6 nhóm RIASEC","Đánh giá 6 khuynh hướng nghề nghiệp phổ biến theo mô hình Holland."),
    ("💼","Ngành & nghề","Đề xuất nhóm ngành, vị trí nghề nghiệp, môn học và kỹ năng nên ưu tiên."),
    ("🚀","Lộ trình hành động","Gợi ý bước tiếp theo trong 7 ngày, 30 ngày và 90 ngày để kiểm chứng lựa chọn."),
]
for col,item in zip([f1,f2,f3,f4],features):
    with col:
        st.markdown(f"""
        <div class="feature-card">
          <div class="feature-icon">{item[0]}</div>
          <div class="feature-title">{item[1]}</div>
          <div class="feature-desc">{item[2]}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Minh họa thêm
i1,i2 = st.columns(2)
with i1:
    st.image(illustration_svg("Khám phá sở thích", "Nhìn rõ điều bạn thực sự hứng thú", "#5B5BD6", "compass"), use_container_width=True)
with i2:
    st.image(illustration_svg("30 câu hỏi ngắn", "Chỉ cần chọn mức độ phù hợp nhất", "#14B8A6", "quiz"), use_container_width=True)

# =========================================================
# THÔNG TIN CÁ NHÂN
# =========================================================
st.markdown('<div class="section-title">1. Thông tin của bạn</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Thông tin chỉ dùng để cá nhân hóa phần kết quả trong phiên làm việc hiện tại.</div>', unsafe_allow_html=True)

c1,c2,c3 = st.columns([1.5,1,1])
with c1:
    name = st.text_input("Họ và tên", placeholder="Ví dụ: Nguyễn Minh Anh")
with c2:
    education = st.selectbox("Trình độ hiện tại", ["THCS","THPT","Sinh viên","Mới tốt nghiệp","Đang đi làm","Khác"])
with c3:
    priority = st.selectbox("Ưu tiên nghề nghiệp", ["Chưa xác định","Thu nhập","Ổn định","Sáng tạo","Cơ hội thăng tiến","Cân bằng cuộc sống","Tác động xã hội"])

# =========================================================
# KHẢO SÁT
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">2. Khảo sát 30 câu hỏi</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Chọn theo cảm nhận tự nhiên. Không có đáp án đúng hoặc sai.</div>', unsafe_allow_html=True)

answers = {}
groups = [
    ("Nhóm 1 · Cách bạn thích làm việc",0,10),
    ("Nhóm 2 · Điều khiến bạn hứng thú",10,20),
    ("Nhóm 3 · Môi trường bạn cảm thấy phù hợp",20,30),
]

for gi,(title,start,end) in enumerate(groups):
    with st.expander(title, expanded=(gi==0)):
        for idx in range(start,end):
            cat,q = questions[idx]
            st.markdown(f"""
            <div class="q-card">
              <span class="q-num">{idx+1}</span>
              <span class="q-text">{q}</span>
            </div>
            """, unsafe_allow_html=True)
            answers[idx] = st.radio(
                f"q{idx+1}",
                [1,2,3,4,5],
                index=2,
                format_func=lambda x: scale_text[x],
                horizontal=True,
                key=f"q_{idx}",
                label_visibility="collapsed",
            )

st.markdown("**Tiến độ khảo sát**")
st.progress(1.0)
st.caption("30/30 câu đã sẵn sàng để phân tích.")

def calculate_scores():
    scores = {k:0 for k in labels}
    for idx,(cat,_) in enumerate(questions):
        scores[cat] += answers[idx]
    percentages = {k: round(v/25*100,1) for k,v in scores.items()}
    ranked = sorted(percentages.items(), key=lambda x:x[1], reverse=True)
    return scores, percentages, ranked

def combo_key(a,b):
    if a+b in combo_suggestions: return a+b
    if b+a in combo_suggestions: return b+a
    return None

if st.button("✨ PHÂN TÍCH KẾT QUẢ NGHỀ NGHIỆP"):
    scores, percentages, ranked = calculate_scores()
    st.session_state["career_result"] = {
        "scores":scores,
        "percentages":percentages,
        "ranked":ranked,
        "name":name.strip() or "Bạn",
        "education":education,
        "priority":priority,
        "time":datetime.now().strftime("%d/%m/%Y %H:%M"),
    }

# =========================================================
# KẾT QUẢ
# =========================================================
if "career_result" in st.session_state:
    result = st.session_state["career_result"]
    ranked = result["ranked"]
    top1,top2,top3 = ranked[:3]

    st.markdown("<br>", unsafe_allow_html=True)
    st.image(illustration_svg("Kết quả của bạn", "Tổng hợp từ 6 nhóm khuynh hướng nghề nghiệp", "#7C3AED", "result"), use_container_width=True)

    st.markdown('<div class="section-title">3. Kết quả định hướng nghề nghiệp</div>', unsafe_allow_html=True)
    st.success(f"{result['name']} có khuynh hướng nổi bật nhất ở nhóm **{labels[top1[0]]}**.")

    m1,m2,m3 = st.columns(3)
    for col,data,rank_name in zip([m1,m2,m3],[top1,top2,top3],["Top 1","Top 2","Top 3"]):
        with col:
            st.markdown(f"""
            <div class="metric-box">
              <div class="metric-val">{data[1]:.0f}%</div>
              <div class="metric-label">{rank_name} · {labels[data[0]]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### Bản đồ 6 nhóm khuynh hướng")
    chart_df = pd.DataFrame({
        "Nhóm":[labels[k] for k,_ in ranked],
        "Mức phù hợp (%)":[v for _,v in ranked],
    }).set_index("Nhóm")
    st.bar_chart(chart_df)

    st.markdown("### 3 hướng nghề nổi bật")
    cols = st.columns(3)
    for i,(cat,pct) in enumerate([top1,top2,top3],start=1):
        info = career_map[cat]
        with cols[i-1]:
            st.image(career_art(info["title"],cat,info["c1"],info["c2"]), use_container_width=True)
            majors = "".join(f'<span class="pill">{x}</span>' for x in info["majors"][:4])
            st.markdown(f"""
            <div class="result-card">
              <div class="rank">Gợi ý #{i} · {pct:.0f}%</div>
              <div class="result-title">{info["title"]}</div>
              <div class="result-desc">{info["desc"]}</div>
              <div style="margin-top:12px">{majors}</div>
            </div>
            """, unsafe_allow_html=True)

    # Phân tích sâu Top 1
    top_info = career_map[top1[0]]
    st.markdown("### Phân tích sâu hướng phù hợp nhất")
    a1,a2 = st.columns(2)
    with a1:
        st.markdown(f"""
        <div class="info-card">
          <div class="feature-title">🏢 Môi trường làm việc phù hợp</div>
          <div class="feature-desc">{top_info["environment"]}</div>
        </div>
        """, unsafe_allow_html=True)
    with a2:
        st.markdown(f"""
        <div class="info-card">
          <div class="feature-title">📚 Môn học nên chú ý</div>
          <div class="feature-desc">{", ".join(top_info["subjects"])}</div>
        </div>
        """, unsafe_allow_html=True)

    b1,b2 = st.columns(2)
    with b1:
        st.markdown("#### Nghề nghiệp nên tham khảo")
        for job in top_info["jobs"]:
            st.markdown(f"- **{job}**")
    with b2:
        st.markdown("#### Kỹ năng nên ưu tiên")
        for skill in top_info["skills"]:
            st.markdown(f"- **{skill}**")

    ck = combo_key(top1[0], top2[0])
    st.markdown("### Hướng kết hợp tiềm năng")
    if ck:
        combo_title, combo_jobs = combo_suggestions[ck]
        st.info(
            f"**{combo_title}** — sự kết hợp giữa **{labels[top1[0]]}** và **{labels[top2[0]]}**. "
            f"Các vai trò có thể tìm hiểu thêm: {', '.join(combo_jobs)}."
        )
    else:
        st.info(
            f"Bạn có sự kết hợp giữa **{labels[top1[0]]}** và **{labels[top2[0]]}**. "
            "Hãy trải nghiệm dự án ngắn hoặc khóa học thử để kiểm chứng mức độ phù hợp."
        )

    # Lộ trình 90 ngày
    st.markdown("### Lộ trình hành động 90 ngày")
    r1,r2,r3 = st.columns(3)
    with r1:
        st.markdown("""
        <div class="roadmap">
          <b>7 ngày đầu</b><br><br>
          • Chọn 2–3 nghề trong Top 1–2<br>
          • Xem 5 mô tả công việc thực tế<br>
          • Ghi lại kỹ năng xuất hiện nhiều nhất
        </div>
        """, unsafe_allow_html=True)
    with r2:
        st.markdown("""
        <div class="roadmap">
          <b>30 ngày</b><br><br>
          • Học thử 1 khóa ngắn<br>
          • Làm 1 dự án nhỏ<br>
          • Trao đổi với người đang làm nghề
        </div>
        """, unsafe_allow_html=True)
    with r3:
        st.markdown("""
        <div class="roadmap">
          <b>90 ngày</b><br><br>
          • Hoàn thiện 1 sản phẩm/portfolio<br>
          • Thử CLB, part-time hoặc thực tập<br>
          • Đánh giá lại mức độ hứng thú
        </div>
        """, unsafe_allow_html=True)

    with st.expander("Xem bảng điểm chi tiết 6 nhóm"):
        detail_df = pd.DataFrame([
            {
                "Mã":cat,
                "Nhóm khuynh hướng":labels[cat],
                "Điểm":result["scores"][cat],
                "Tối đa":25,
                "Mức phù hợp":f"{result['percentages'][cat]:.1f}%"
            }
            for cat,_ in ranked
        ])
        st.dataframe(detail_df, use_container_width=True, hide_index=True)

    export_df = pd.DataFrame([
        {
            "Ho_ten":result["name"],
            "Trinh_do":result["education"],
            "Uu_tien":result["priority"],
            "Ma_RIASEC":cat,
            "Nhom":labels[cat],
            "Diem":result["scores"][cat],
            "Muc_phu_hop_%":result["percentages"][cat],
            "Thoi_gian":result["time"]
        }
        for cat,_ in ranked
    ])
    csv_data = export_df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "⬇️ TẢI KẾT QUẢ CSV",
        data=csv_data,
        file_name=f"ket_qua_dinh_huong_nghe_{result['name'].replace(' ','_')}.csv",
        mime="text/csv"
    )

    st.markdown("""
    <div class="notice">
      <b>Lưu ý:</b> Kết quả mang tính định hướng tham khảo dựa trên mô hình RIASEC.
      Bạn nên kết hợp thêm năng lực học tập, trải nghiệm thực tế, điều kiện cá nhân và thông tin thị trường lao động trước khi quyết định ngành học hoặc nghề nghiệp.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align:center;color:#98A2B3;font-size:13px;padding:18px 0">
  {APP_NAME} · {APP_TITLE} · Streamlit
</div>
""", unsafe_allow_html=True)

import streamlit as st

# がん検診推奨情報（例。実際の推奨年齢等は公式情報を参照してください）
recommended_screenings = [
    {
        "name": "胃がん検診",
        "sex": "男女",
        "age_min": 50,
        "age_max": 75,
        "reason": "胃がんは早期発見で治療成績が大きく向上します。定期的な検診で無症状のうちに発見できる可能性があります。"
    },
    {
        "name": "大腸がん検診",
        "sex": "男女",
        "age_min": 40,
        "age_max": 75,
        "reason": "大腸がんは日本人に多く、便潜血検査で早期発見が可能です。"
    },
    {
        "name": "肺がん検診",
        "sex": "男女",
        "age_min": 40,
        "age_max": 75,
        "reason": "肺がんはがん死亡原因の上位です。喫煙歴がある方は特に検診が重要です。"
    },
    {
        "name": "乳がん検診",
        "sex": "女性",
        "age_min": 40,
        "age_max": 74,
        "reason": "乳がんは女性のがんの中で最も多く、早期発見で治療成績が向上します。"
    },
    {
        "name": "子宮頸がん検診",
        "sex": "女性",
        "age_min": 20,
        "age_max": 65,
        "reason": "子宮頸がんは若い世代にも増えています。定期検診で早期発見が可能です。"
    },
]

st.title("厚生労働省推奨のがん検診案内チャットボット")

# ユーザー入力
age = st.number_input("あなたの年齢を入力してください", min_value=0, max_value=120, value=40)
sex = st.selectbox("あなたの性別を選択してください", ("男性", "女性"))

# 対象となる検診一覧を作成
target_screenings = []
for s in recommended_screenings:
    if (s["sex"] == "男女" or (sex == "女性" and s["sex"] == "女性")) \
            and (s["age_min"] <= age <= s["age_max"]):
        target_screenings.append(s["name"])

checked = st.multiselect("すでに受けたがん検診を選択してください", target_screenings)

# 未受診の検診を判定
not_checked = [s for s in target_screenings if s not in checked]

if st.button("未受診のがん検診の理由を表示"):
    if not_checked:
        st.write("以下の検診はまだ受けていません。受診をおすすめする理由：")
        for s in recommended_screenings:
            if s["name"] in not_checked:
                st.markdown(f"- **{s['name']}**: {s['reason']}")
    else:
        st.success("推奨されるがん検診はすべて受診済みです。")

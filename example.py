import openthaigpt

print(openthaigpt.generate("Q: อยากลดความอ้วนทำไง\n\nA:"))
# Q: อยากลดความอ้วนทำไง
#
# A: การลดน้ำหนักเป็นสิ่งที่สำคัญที่สุดสำหรับการลดไขมันในร่างกาย ดังนั้นคุณควรปรึกษาแพทย์หรือผู้เชี่ยวชาญด้านสุขภาพก่อนที่จะตัดสินใจว่าจะเลือกใช้ผลิตภัณฑ์ใดในการรักษาหรือไม่ อย่างไรก็ตาม หากคุณรู้สึกว่าตัวเองมีปัญหาในเรื่องนี้ คุณสามารถติดต่อแพทย์เพื่อสอบถามข้อมูลเพิ่มเติมเกี่ยวกับวิธีการแก้ไขปัญหานี้ได้เช่นกัน นอกจากนี้คุณยังสามารถพูดคุยกับคนอื่น ๆ เพื่อช่วยให้คำปรึกษาที่ดียิ่งขึ้นได้อีกด้วยค่ะ ขอบคุณที่มา: https://www.facebook.com/pages/%E0%B8%A8-in-the-circle-healthy-make-up.html?mibextid=a&browse=b&country=1&fb=&idx=0&pageb

# ข้อความจาก OpenThaiGPT
openthaigpt.zero("การลดน้ำหนักเป็นเรื่องที่ต้องพิจารณาอย่างละเอียดและรอบคอบเพื่อให้ได้ผลลัพธ์ที่ดีและมีประสิทธิภาพมากที่สุด")
# {'perplexity': 2.4544131755828857,
# 'threshold': 10,
# 'isGeneratedFromOpenThaiGPT': True}

# ข้อความจาก OpenAI ChatGPT
openthaigpt.zero("สวัสดีครับ มีอะไรให้ผมช่วยเหลือหรือไม่ครับ?")
# {'perplexity': 4.949122428894043,
# 'theshold': 10,
# 'isGeneratedFromOpenThaiGPT': True}

# ข้อความจากมนุษย์
openthaigpt.zero("ทดสอบครับผม")
# {'perplexity': 1758.141357421875,
# 'threshold': 10,
# 'isGeneratedFromOpenThaiGPT': False}

# แสดงวิธีการปรับ threshold
openthaigpt.zero("สวัสดีครับ", threshold=5)
# {'perplexity': 8.109768867492676,
# 'theshold': 5,
# 'isGeneratedFromOpenThaiGPT': False}
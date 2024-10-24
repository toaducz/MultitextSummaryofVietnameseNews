"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

from google.generativeai.types import HarmCategory, HarmBlockThreshold



# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
def gemini_api(source_text,key):
  os.environ["GEMINI_API_KEY"] = key

  genai.configure(api_key=os.environ["GEMINI_API_KEY"])

  generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 4096,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings={
          HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
          HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
          HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
          HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
      }
  )
  chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Dịch bài báo sang tiếng việt, thêm 1 câu tóm tắt nội dung vào đầu đoạn\n\"Tây Ninh Province police are coordinating with the police of Hoa Thanh Town and relevant units to investigate a case in which three people died in a house fire. The incident was reported to the local authorities and Fire Prevention and Fighting Police Team of Hoa Thanh Town Police to help control the blaze. The fire was extinguished after about 30 minutes, at that time, three people were confirmed dead inside. The victims were identified as the homeowner, Ms. P.T.T.T. (44 years old), Mr. N.T.D. (46 years old, residing in Go Dau District), and Ms. N.T.L. (55 years old, residing in Hoa Thanh Town). According to the initial investigation results, the house where the fire occurred had a bedroom, a gate, and an iron entrance door, all locked from the inside. The three bodies were found in the bedroom, surrounded by pieces of burnt plastic with a smell of gasoline. Through autopsy, the investigation agency determined that Ms. T. and Ms. L. died of head injuries, while Mr. D. died of burns. The police initially determined that this was a murder case due to a love triangle. Specifically, Mr. D. used a blunt object to kill the two women, then bought gasoline, locked the door, and set the house on fire. The investigation agency is currently clarifying related issues.\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Cảnh sát tỉnh Tây Ninh đang điều tra vụ cháy nhà khiến ba người tử vong, nghi có liên quan đến tình tay ba.\n\nCông an tỉnh Tây Ninh phối hợp với Công an thị trấn Hòa Thành và các đơn vị liên quan điều tra vụ cháy nhà khiến ba người tử vong. Vụ cháy được báo về chính quyền địa phương và Đội Cảnh sát phòng cháy chữa cháy Công an thị trấn Hòa Thành đã đến hiện trường dập lửa. Sau khoảng 30 phút, ngọn lửa được dập tắt, thời điểm này, người dân phát hiện thi thể ba nạn nhân tử vong tại hiện trường. Nạn nhân được xác định gồm chủ nhà bà P.T.T.T. (44 tuổi), anh N.T.D. (46 tuổi, ngụ huyện Gò Dầu) và bà N.T.L. (55 tuổi, ngụ thị trấn Hòa Thành). Theo kết quả điều tra ban đầu, ngôi nhà xảy ra hỏa hoạn có một phòng ngủ, cổng và cửa sắt ra vào đều được khóa từ bên trong. Ba thi thể được phát hiện ở phòng ngủ, xung quanh có nhiều mảnh nhựa cháy kèm theo mùi xăng. Qua khám nghiệm tử thi, cơ quan điều tra xác định bà T. và bà L. tử vong do chấn thương vùng đầu, còn anh D. tử vong do bị cháy. Bước đầu, cơ quan công an xác định đây là vụ án mạng có nguyên nhân từ mâu thuẫn tình cảm. Cụ thể, anh D. đã dùng vật tày đập chết hai người phụ nữ, sau đó mua xăng, khóa cửa rồi phóng hỏa căn nhà. Hiện, cơ quan điều tra đang tiếp tục làm rõ các tình tiết liên quan.",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Dịch bài báo sang tiếng việt, thêm 1 câu tóm tắt nội dung vào đầu đoạn\n\"The Da Nang Radiation Technology Research and Deploment Center (Hoa Son commune, Hoa Vang district), was involved in an incident of a Co-60 source being hooked into a container going out of the irradiation chamber, causing loss of security. The drill was organized by the Da Nang City Department of Science and Technology over the weekend, at an industrial irradiation facility using Group A radioactive sources - the highest level among radioactive sources. The drill was organized by the Da Nang City Department of Science and Technology over the weekend, at an industrial irradiation facility using Group A radioactive sources - the highest level among radioactive sources. The forces of the police, rescue and rescue, and the City's Radiation and Nuclear Incident Response Steering Committee met to discuss the incident handling plan. The forces of the police, rescue and rescue, and the City's Radiation and Nuclear Incident Response Steering Committee met to discuss the incident handling plan. Entry and exit to the dangerous area is set up by the technical support unit, using specialized equipment to check radiation safety. Entry and exit to the dangerous area is set up by the technical support unit, using specialized equipment to check radiation safety. The medical force is present to provide first aid and care for victims affected after the incident. Robot VINA-Res was mobilized to move into the irradiation chamber to pick up the source bar hooked into the cargo container and drop it into the source tank to reduce the dose rate in the cargo irradiation area to normal levels. Radiation from the source bar caused the cargo container to catch fire, beyond the response capabilities of the facility, so the Center reported and requested assistance from the authorities. After the source bar was placed in the source tank, the fire prevention and firefighting force and rescue team controlled the fire. When the fire is under control, the technical support force wearing specialized anti-radiation clothing enters the area to measure and assess the radioactive contamination status in the irradiation chamber area. Chemical soldiers decontaminate objects contaminated with radioactive contamination and surrounding areas to ensure safety at the scene of the incident. Radioactive waste is moved out. The incident area is also scanned before the scene is handed over. After completing the decontamination, the fire prevention and fighting police force, the army and people present in the isolation area took\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Trung tâm Nghiên cứu ứng dụng công nghệ bức xạ Đà Nẵng (xã Hòa Sơn, huyện Hòa Vang) xảy ra sự cố nguồn Co-60 bị mắc vào container khi ra khỏi buồng chiếu xạ, mất an toàn.\n\nCuộc diễn tập do Sở Khoa học và Công nghệ TP Đà Nẵng tổ chức vào cuối tuần qua, tại cơ sở chiếu xạ công nghiệp sử dụng nguồn phóng xạ nhóm A - nhóm cao nhất trong các nhóm nguồn phóng xạ. Lực lượng công an, cứu nạn cứu hộ, Ban chỉ đạo ứng phó sự cố bức xạ hạt nhân thành phố họp bàn phương án xử lý sự cố. Lực lượng công an, cứu nạn cứu hộ, Ban chỉ đạo ứng phó sự cố bức xạ hạt nhân thành phố họp bàn phương án xử lý sự cố. Đơn vị hỗ trợ kỹ thuật lập chốt an toàn ra vào khu vực nguy hiểm và sử dụng trang thiết bị chuyên dụng kiểm tra an toàn bức xạ. Đơn vị hỗ trợ kỹ thuật lập chốt an toàn ra vào khu vực nguy hiểm và sử dụng trang thiết bị chuyên dụng kiểm tra an toàn bức xạ. Lực lượng y tế túc trực, sơ cấp cứu nạn nhân bị ảnh hưởng sau sự cố. Robot VINA-Res được huy động vào buồng chiếu để gắp thanh nguồn mắc vào container hàng, thả thanh nguồn về hố chứa nguồn giúp đưa mức liều tại khu vực chiếu hàng hóa về mức bình thường. Bức xạ rò rỉ từ thanh nguồn khiến container hàng bốc cháy, vượt quá khả năng ứng cứu của đơn vị nên Trung tâm đã báo cáo và đề nghị các lực lượng có thẩm quyền hỗ trợ. Sau khi thanh nguồn được đưa về hố chứa, lực lượng phòng cháy chữa cháy, cứu nạn cứu hộ triển khai khống chế đám cháy. Khi đám cháy được khống chế, lực lượng hỗ trợ kỹ thuật mặc đồ bảo hộ chống bức xạ chuyên dụng vào khu vực để đo đạc, đánh giá tình trạng nhiễm bẩn phóng xạ tại khu vực buồng chiếu. Binh hóa học thực hiện khử nhiễm các đồ vật bị nhiễm bẩn phóng xạ và khu vực xung quanh để đảm bảo an toàn tại hiện trường sự cố. Chất thải phóng xạ được chuyển đi. Khu vực xảy ra sự cố cũng được rà quét trước khi bàn giao hiện trường. Sau khi hoàn thành công tác khử nhiễm, lực lượng cảnh sát phòng cháy chữa cháy, quân đội, dân quân có mặt tại khu vực cách ly đã thực hiện.",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Dịch bài báo sang tiếng việt, thêm 1 câu tóm tắt nội dung vào đầu đoạn\n\"The Ministry of National Defense has issued a reply to the petition of voters in Vinh Phuc province, proposing amendments to the Law on Military Service. The Law on Military Service has made an important contribution to implementing military and defense tasks of localities and units, and enhancing the combat strength of the army. However, the actual implementation process still has shortcomings, especially in the management of citizens of military age for students who are called for military service and temporarily deferred from military service. The Ministry of National Defense admits that there are some cases that are granted additional time to study, being held back, failing subjects, or retaking graduation exams, or who finish school but do not go on military service, or go to a new place of residence. This content has not yet had full regulations and sanctions, leading to taking advantage of evading military service, causing difficulties in management and public outrage. The Ministry of National Defense will continue to study, adjust the support levels, and make proposals when amending the Law on Military Service.\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Bộ Quốc phòng đã có văn bản trả lời đơn kiến nghị của cử tri tỉnh Vĩnh Phúc kiến nghị sửa đổi Luật nghĩa vụ quân sự.\n\nLuật nghĩa vụ quân sự đã có những đóng góp quan trọng vào việc thực hiện nhiệm vụ quân sự, quốc phòng của các địa phương, đơn vị, góp phần nâng cao sức mạnh chiến đấu của quân đội. Tuy nhiên, trong quá trình thực hiện vẫn còn một số tồn tại, nhất là công tác quản lý công dân trong độ tuổi thực hiện nghĩa vụ quân sự là sinh viên, học viên đang được hoãn thực hiện nghĩa vụ quân sự. Bộ Quốc phòng thừa nhận thực tế vẫn có một số trường hợp được tạo điều kiện để tiếp tục học, học lại, học vượt, thi lại tốt nghiệp... hoặc học xong không thực hiện nghĩa vụ quân sự, hoặc chuyển hộ khẩu đi nơi khác. Nội dung này vẫn chưa có chế tài quản lý, xử lý cụ thể, dẫn đến tình trạng lợi dụng để trốn tránh nghĩa vụ quân sự, gây khó khăn trong công tác quản lý và bức xúc trong dư luận xã hội. Bộ Quốc phòng sẽ tiếp tục nghiên cứu, điều chỉnh mức hỗ trợ, định mức hỗ trợ và trình đề xuất khi sửa đổi Luật nghĩa vụ quân sự.",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Dịch bài báo sang tiếng việt, thêm 1 câu tóm tắt nội dung vào đầu đoạn:\n\"General Secretary Nguyen Phu Trong passed away on July 19 at the age of 80 due to old age and illnesses. His funeral will be held with State funeral honours on July 25-26, after which he will be interred at Mai Dich Cemetery. Condolence book for General Secretary Nguyen Phu Trong Ngoc Anh ||| 22 Airports To Screen Documentary About General Secretary Nguyen Phu Trong On the evening of July 23, a representative of Vietnam Airports Corporation (ACV) said that starting today, 22 airports across the country will screen a documentary about the life and career of General Secretary Nguyen Phu Trong. These are documentary films and images about General Secretary Nguyen Phu Trong produced by media agencies and will be screened on public screens at 22 airports nationwide throughout the national mourning period. Since July 20, not only Tan Son Nhat and Noi Bai airports, but also airports across the country have turned off vibrant advertisements on public screens, suspended cultural and sports activities, and flown flags at half-mast. According to the ACV representative, the Corporation has also asked units to increase the allocation of resources (infrastructure, equipment, personnel) to prepare the best conditions to serve the flights carrying domestic and international delegations attending the national funeral. Earlier, Director of the Civil Aviation Authority of Vietnam Dinh Viet Thang issued a decision to apply enhanced level-1 aviation security control measures at airports, heliports, air traffic services providers, airlines, and aviation service providers during the organization of General Secretary Nguyen Phu Trong's state funeral. Accordingly, the implementation time is from 5:00 PM on July 22, 2024 to 12:00 AM on July 26, 2024.\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Tổng Bí thư Nguyễn Phú Trọng từ trần hồi 80 tuổi do tuổi cao sức yếu và bệnh tật. Lễ tang được cử hành theo nghi thức Quốc tang trong 2 ngày 25 và 26/7, sau đó an táng tại Nghĩa trang Mai Dịch. Vở chia buồn Tổng bí thư Nguyễn Phú Trọng Ngọc Anh (ghi) ||| 22 cảng hàng không chiếu phim tư liệu về Tổng Bí thư Nguyễn Phú Trọng Tối 23/7, đại diện Tổng công ty Cảng hàng không Việt Nam (ACV) cho biết từ hôm nay 22 cảng hàng không trên toàn quốc sẽ chiếu phim tư liệu về cuộc đời và sự nghiệp của Tổng Bí thư Nguyễn Phú Trọng. Đây là những bộ phim tài liệu, hình ảnh về Tổng Bí thư Nguyễn Phú Trọng do các cơ quan báo chí thực hiện và sẽ được chiếu trên màn hình công cộng tại 22 cảng hàng không trên toàn quốc trong suốt thời gian quốc tang. Từ ngày 20/7, không chỉ sân bay Tân Sơn Nhất, Nội Bài, mà các cảng hàng không trên toàn quốc đã tắt các hình ảnh quảng cáo sôi động trên màn hình công cộng, tạm dừng các hoạt động văn hóa, thể thao, treo cờ rủ. Theo đại diện ACV, Tổng công ty cũng đã yêu cầu các đơn vị tăng cường bố trí nguồn lực (cơ sở vật chất, phương tiện, nhân lực) để chuẩn bị điều kiện phục vụ tốt nhất cho các chuyến bay đưa đón các đoàn đại biểu trong và ngoài nước tới dự tang lễ cấp cao. Trước đó, Cục trưởng Cục Hàng không Việt Nam Đinh Việt Thắng đã ký Quyết định áp dụng biện pháp kiểm soát an ninh hàng không cấp độ 1 tăng cường tại các cảng hàng không, cảng trực thăng, đơn vị cung cấp dịch vụ điều hành bay, các hãng hàng không và đơn vị cung cấp dịch vụ trên địa bàn trong thời gian tổ chức tang lễ cấp nhà nước đối với Tổng Bí thư Nguyễn Phú Trọng. Theo đó, thời gian thực hiện từ 17h00 ngày 22/7/2024 đến hết 24h00 ngày 26/7/2024.",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Dịch bài báo sang tiếng việt, thêm 1 câu tóm tắt nội dung vào đầu đoạn:\n\"General Secretary Nguyen Phu Trong is an exceptionally outstanding leader, a bright example of learning, following the ideology, morality, and style of Ho Chi Minh, fully embodying the qualities, talents, mettle, and wisdom of the generation of Vietnamese leaders in the period of renewal, wholeheartedly and devotedly serving the Fatherland, serving the people, with great prestige and influence both at home and abroad, making great contributions and dedications to the revolutionary cause of the Party, State, and our people as well as to peace, cooperation, and development in the region and the world. In the midst of our infinite sorrow over the passing of General Secretary Nguyen Phu Trong, we remember and cherish even more the shining moral example of a great personality with a keen theoretical mind, who left behind a great legacy and made immense contributions and dedications to the cause of building, developing, and defending the Vietnamese Fatherland in the period of renewal. That is to steadfastly follow, creatively apply, and develop Marxism-Leninism, Ho Chi Minh's thought, in conjunction with promoting the fine cultural traditions of the nation and inheriting the quintessence of human wisdom; to remain steadfast in the goal of national independence and socialism; to remain steadfast in the renewal policy; to remain steadfast in the principles of organization and operation of the Party, which are clearly reflected in the Party's resolutions through its congresses, the resolutions of the Central Committee, and summarized and systematized in the great theoretical works and projects of General Secretary Nguyen Phu Trong, especially the article \"Some theoretical and practical issues on socialism and the path to socialism in Vietnam\" on the occasion of the 131st anniversary of President Ho Chi Minh's birth. That is to steadfastly follow, creatively apply, and develop Marxism-Leninism, Ho Chi Minh's thought, in conjunction with promoting the fine cultural traditions of the nation and inheriting the quintessence of human wisdom; to remain steadfast in the goal of national independence and socialism; to remain steadfast in the renewal policy; to remain steadfast in the principles of organization and operation of the Party, which are clearly reflected in the Party's\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Tổng Bí thư Nguyễn Phú Trọng là nhà lãnh đạo đặc biệt kiệt xuất, tấm gương sáng về học tập và làm theo tư tưởng, đạo đức, phong cách Hồ Chí Minh, thể hiện đầy đủ phẩm chất, tài năng, bản lĩnh, trí tuệ của lớp lãnh đạo cách mạng Việt Nam thời kỳ đổi mới, trọn đời tận trung với nước, tận hiếu với dân, có uy tín rất cao, tầm ảnh hưởng lớn trong nước và quốc tế, có nhiều công lao, đóng góp to lớn đối với sự nghiệp cách mạng của Đảng, Nhà nước và nhân dân ta, đối với hòa bình, hợp tác, phát triển ở khu vực và trên thế giới. Trong niềm tiếc thương vô hạn trước sự ra đi của Tổng Bí thư Nguyễn Phú Trọng, chúng ta càng thêm tưởng nhớ, trân trọng trước tấm gương đạo đức sáng ngời của một nhân cách lớn, trí tuệ lý luận sắc sảo, để lại di sản đồ sộ, có nhiều đóng góp, cống hiến to lớn cho sự nghiệp xây dựng, phát triển và bảo vệ Tổ quốc Việt Nam trong thời kỳ đổi mới. Đó là nhất quán trung thành với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh, kết hợp với phát huy những giá trị truyền thống tốt đẹp của dân tộc, tiếp thu tinh hoa trí tuệ nhân loại; kiên định mục tiêu độc lập dân tộc gắn liền với chủ nghĩa xã hội; kiên định đường lối đổi mới; kiên định nguyên tắc tổ chức, hoạt động của Đảng, được thể hiện đầy đủ trong các nghị quyết, nghị luận của Đảng qua các kỳ đại hội, các khóa Trung ương, được Tổng Bí thư Nguyễn Phú Trọng khái quát, hệ thống hóa trong các công trình, dự án lý luận lớn, đặc biệt là bài viết \"Một số vấn đề lý luận và thực tiễn về chủ nghĩa xã hội và con đường đi lên chủ nghĩa xã hội ở Việt Nam\" nhân kỷ niệm 131 năm Ngày sinh của Chủ tịch Hồ Chí Minh. Đó là nhất quán trung thành với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh, kết hợp với phát huy những giá trị truyền thống tốt đẹp của dân tộc, tiếp thu tinh hoa trí tuệ nhân loại; kiên định mục tiêu độc lập dân tộc gắn liền với chủ nghĩa xã hội; kiên định đường lối đổi mới; kiên định nguyên tắc tổ chức, hoạt động của Đảng, được thể hiện đầy đủ trong các nghị quyết, nghị luận của Đảng qua các kỳ đại hội, các khóa Trung ương, được Tổng Bí thư",
      ],
    },
  ]
)
  temp = chat_session.send_message("Dịch bài báo sang tiếng việt, thêm 1 câu tóm tắt nội dung vào đầu đoạn:\n\ " + source_text)
  return temp.text
 
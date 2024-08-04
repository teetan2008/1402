from zlapi import ZaloAPI
from zlapi.models import Message
import requests
from getid import getuid
from apicntfb import checkid
from share import run
from time import sleep
import threading

class TeeTan(ZaloAPI):
    def __init__(self, phone, passzl, imei, session_cookies):
        super().__init__(phone, passzl, imei=imei, session_cookies=session_cookies)
        self.share = False
        self.allow_group=[]

    def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type):
        try:
            if author_id != self.uid and thread_id in self.allow_group or author_id == '6949019840942160627':
                self.markAsDelivered(mid, message_object.cliMsgId, author_id, thread_id, thread_type, message_object.msgType)
                self.markAsRead(mid, message_object.cliMsgId, author_id, thread_id, thread_type, message_object.msgType)
                
                print(f"Received message: {message} from {author_id} in thread {thread_id}, type {thread_type}, {message_object}")
                
                # If message is not a string, set message to "[not a message]"
                if not isinstance(message, str):
                    message = "[not a message]"
                
                # Echo back if the message starts with 'Bot'
                
                if message.startswith('Bot'):
                    reply = 'Hello My Fen'
                    self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                
                # Share a post if the message starts with 'Share' and author_id matches admin_id
                admin_id = '6949019840942160627'  # Replace with your actual admin ID
                if author_id == admin_id and message.startswith('Addgroup'):
                  id_group=message.split()[1]
                  self.allow_group.append(id_group)
                  print(self.allow_group)
                  reply=f'Đã thêm thành công bot vào nhóm có ID : {id_group}'
                  self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                if message.startswith('Share'):
                    if self.share:
                        reply = 'Đang Có Đơn Chưa Hoàn Thành. Vui Lòng Đợi Trong Vài Phút🤧🤧'
                        self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                        return
                    else:
                        try:
                            id_post = message.split()[1]
                            lan = int(message.split()[2])
                            if lan > 100:
                                reply = 'Max 100'
                                self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                                return
                            
                            cookies = {
    'sb': 'CXFQZrhBv5wvu9ymVgBTt-dS',
    'datr': 'CXFQZtGEiL6df3lh9J2Z6CfZ',
    'ps_n': '1',
    'ps_l': '1',
    'c_user': '100001501990613',
    'dpr': '1.875',
    'm_page_voice': '100001501990613',
    'locale': 'vi_VN',
    'vpd': 'v1%3B752x384x1.875',
    'fbl_st': '101523121%3BT%3A28712292',
    'wl_cbv': 'v2%3Bclient_version%3A2577%3Btimestamp%3A1722737535',
    'xs': '37%3A0qcXzcwSvczaLQ%3A2%3A1716692043%3A-1%3A6285%3A%3AAcVq7sQ-YttER7kw5hCCcE-bFc_jEG3DFTiVsEtVmw',
    'fr': '1UNVNfZRhYPEIEmdi.AWUyvlYI2lSNlPpZRfXXqrCmPsA.BmruOB..AAA.0.0.BmruOE.AWU7BF5ENto',
    'wd': '980x1919',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1722737554910%2C%22v%22%3A1%7D',
}
                            headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    # 'cookie': 'sb=CXFQZrhBv5wvu9ymVgBTt-dS; datr=CXFQZtGEiL6df3lh9J2Z6CfZ; ps_n=1; ps_l=1; c_user=100001501990613; dpr=1.875; m_page_voice=100001501990613; locale=vi_VN; vpd=v1%3B752x384x1.875; fbl_st=101523121%3BT%3A28712292; wl_cbv=v2%3Bclient_version%3A2577%3Btimestamp%3A1722737535; xs=37%3A0qcXzcwSvczaLQ%3A2%3A1716692043%3A-1%3A6285%3A%3AAcVq7sQ-YttER7kw5hCCcE-bFc_jEG3DFTiVsEtVmw; fr=1UNVNfZRhYPEIEmdi.AWUyvlYI2lSNlPpZRfXXqrCmPsA.BmruOB..AAA.0.0.BmruOE.AWU7BF5ENto; wd=980x1919; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1722737554910%2C%22v%22%3A1%7D',
    'dpr': '1.875',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'sec-ch-ua-full-version-list': '"Chromium";v="105.0.5195.32", "Not)A;Brand";v="8.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'viewport-width': '980',
}
                            response = requests.get(f'https://m.facebook.com/{id_post}', cookies=cookies, headers=headers).url
                            if 'watch' in response:
                                reply = 'Không thể buff share ảo cho videos. Nếu muốn buff share ảo cho videos thì gỡ videos đi buff xong rồi edit lại!'
                                self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                                return
                            
                            if 'posts' in response or 'photo' in response:
                                self.share = True
                                reply = f'Đơn tiếp theo cho ID {id_post}'
                                self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                            
                                
                                def f():
                                    try:
                                        result = run(id_post, lan)
                                        if result:
                                            reply = f'Tăng thành công {lan} shares cho ID {id_post}'
                                        else:
                                            reply = f'Tăng thất bại shares cho ID {id_post}'
                                    except Exception as e:
                                        reply = 'Xảy ra lỗi trong quá trình xử lý.'
                                        print(e)
                                    finally:
                                        self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                                        self.share = False
                                
                                m = threading.Thread(target=f)
                                m.start()
                            else:
                              reply='Id_Post không thể xác định'
                              self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                        except Exception as e:
                            print(e)
                            reply = 'Buff Share Ảo Free Cho Ae\nCách Dùng : Share id_post số_lần\nMax: 100\nLưu Ý: Không dùng cho videos, muốn dùng cho videos cần gỡ videos rồi buff xong edit lại!'
                            self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
    
                  
                # Check FB profile if message starts with 'Fb'
                if message.startswith('Fb'):
                    try:
                        uid = message.split()[1]
                        # Assuming checkid function returns a dictionary with profile details
                        # Replace with actual implementation of checkid
                        check = checkid(uid)
                        reply = f'✅️CHECK SUCCESS✅️\n Uid: {check["idfb"]}\n Ngày Tạo: {check["created_time"]}\n Link Fb: {check["link"]}\n Tên Fb: {check["name"]}\n Quê Quán: {check["hometown"]}\n User: {check["username"]}\n Quốc Gia: {check["locale"]}\n Nơi Ở: {check["location"]}\n Web: {check["website"]}\n Giới Tính: {check["gender"]}\n Mối Quan Hệ: {check["relationship_status"]}\n Lượt Theo Dõi: {check["subscribers"]}\n Họ: {check["first_name"]}\n Ngày Sinh: {check["birthday"]}'
                        self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                    
                    except Exception as e:
                        print(e)
                        reply = 'CÁCH SỬ DỤNG: Fb IDFB[Người Cần Check]'
                        self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
        
        except Exception as e:
            print(e)
            reply = 'Bot đã xảy ra sự cố không xác định!'
            self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)

# Initialize and start listening
client = TeeTan('</>', '</>', "a364337f-ace0-4285-8c97-a087533c4339-b78b4e2d6c0a362c418b145fe44ed73f", {"_ga":"GA1.2.854110349.1722652265","_gid":"GA1.2.1164327188.1722652265","_ga_VM4ZJE1265":"GS1.2.1722652265.1.0.1722652265.0.0.0","_ga_RYD7END4JE":"GS1.2.1722652267.1.1.1722652268.59.0.0","_zlang":"vn","zpsid":"Bjyp.362016986.0.fwOPea697CERUO_MJOaSmpJwRl1tkopoTx0azMl-a-PoPqHUG2oARYU97CC","zpw_sek":"gW9T.362016986.a0.B40yVIlaThBn5EMd2kHsib364za9tbJ7GRqZncNH8jSPhnkA6A0r-6YU6efSsKkGLiu1FGxNcEgsvT0aXe9siW","__zi":"3000.SSZzejyD6zOgdh2mtnLQWYQN_RAG01ICFjIXe9fEM8yuc-sYcaLGY7AJugRKGbA8SfFZfpCv.1","__zi-legacy":"3000.SSZzejyD6zOgdh2mtnLQWYQN_RAG01ICFjIXe9fEM8yuc-sYcaLGY7AJugRKGbA8SfFZfpCv.1","ozi":"2000.QOBlzDCV2uGerkFzm09LrMNTvFd62LVGBj_b_eWELT0kt-J_Cpa.1","app.event.zalo.me":"7370408023715644353"})
print('Bot ID:', client.uid)
client.listen()

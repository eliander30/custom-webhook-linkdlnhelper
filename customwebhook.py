from flask import Flask, request, abort
from waitress import serve
import os
import csv

app = Flask(__name__)

@app.route("/customwebhook", methods=['POST'])
def webhook():
	if request.method == 'POST':
                listdata = []
                path = '/var/www/html/webhookfiles'
                filename = "customwebhook.csv"
                complete = os.path.join(path, filename)
                content = request.json
                print("GOT DATA TO TRANSFORM")
                listdata.append(str(content['id']))
                listdata.append(str(content['id_type']))
                listdata.append(str(content['public_id']))
                listdata.append(str(content['hash_id']))
                listdata.append(str(content['member_id']))
                listdata.append(str(content['sn_member_id']))
                listdata.append(str(content['sn_hash_id']))
                listdata.append(str(content['r_member_id']))
                listdata.append(str(content['t_hash_id']))
                listdata.append(str(content['avatar_id']))
                listdata.append(str(content['public_id_2']))
                listdata.append(str(content['lh_id']))
                listdata.append(str(content['profile_url']))
                listdata.append(str(content['email']))
                listdata.append(str(content['third_party_email_1']))  
                listdata.append(str(content['third_party_email_source_1']))
                listdata.append(str(content['third_party_email_is_valid_1']))
                key2 = 'third_party_email_2'
                if key2 in content.keys():
                    listdata.append(content['third_party_email_2'])
                else:
                    listdata.append("None")
                key3 = 'third_party_email_source_2'
                if key3 in content.keys():
                    listdata.append(content['third_party_email_source_2'])
                else:
                    listdata.append("None")
                key4 = 'third_party_email_is_valid_2'
                if key4 in content.keys():
                    listdata.append(content['third_party_email_is_valid_2'])
                else:
                    listdata.append("None")
                listdata.append(str(content['full_name']))
                listdata.append(str(content['first_name']))
                listdata.append(str(content['last_name']))
                listdata.append(str(content['original_first_name']))
                listdata.append(str(content['original_last_name']))
                listdata.append(str(content['custom_first_name']))
                listdata.append(str(content['custom_last_name']))
                listdata.append(str(content['avatar']))
                listdata.append(str(content['headline']))
                listdata.append(str(content['location_name']))
                listdata.append(str(content['industry']))
                listdata.append(str(content['summary']))
                listdata.append(str(content['address']))
                listdata.append(str(content['birthday']))
                listdata.append(str(content['badges_premium']))
                listdata.append(str(content['badges_influencer']))
                listdata.append(str(content['badges_job_seeker']))
                listdata.append(str(content['badges_open_link']))
                listdata.append(str(content['current_company']))
                listdata.append(str(content['current_company_custom']))
                listdata.append(str(content['current_company_position']))
                listdata.append(str(content['current_company_custom_position']))
                listdata.append(str(content['organization_1']))  
                listdata.append(str(content['organization_id_1']))
                listdata.append(str(content['organization_url_1']))
                listdata.append(str(content['organization_title_1']))
                listdata.append(str(content['organization_start_1']))
                listdata.append(str(content['organization_end_1']))
                listdata.append(str(content['organization_description_1']))
                listdata.append(str(content['organization_location_1']))
                listdata.append(str(content['organization_website_1']))
                listdata.append(str(content['organization_domain_1']))
                key5 = 'organization_2'
                if key5 in content.keys():
                    listdata.append(content['organization_2'])
                else:
                    listdata.append("None")
                key6 = 'organization_id_2'
                if key6 in content.keys():
                    listdata.append(content['organization_id_2'])
                else:
                    listdata.append("None")
                key7 = 'organization_url_2'
                if key7 in content.keys():
                    listdata.append(content['organization_url_2'])
                else:
                    listdata.append("None")
                key11 = 'organization_title_2'
                if key11 in content.keys():
                    listdata.append(content['organization_title_2'])
                else:
                    listdata.append("None")
                key12 = 'organization_id_start_2'
                if key12 in content.keys():
                    listdata.append(content['organization_id_start_2'])
                else:
                    listdata.append("None")
                key13 = 'organization_end_2'
                if key13 in content.keys():
                    listdata.append(content['organization_end_2'])
                else:
                    listdata.append("None")
                key14 = 'organization_description_2'
                if key14 in content.keys():
                    listdata.append(content['organization_description_2'])
                else:
                    listdata.append("None")
                key15 = 'organization_location_2'
                if key15 in content.keys():
                    listdata.append(content['organization_location_2'])
                else:
                    listdata.append("None")
                key16 = 'organization_website_2'
                if key16 in content.keys():
                    listdata.append(content['organization_website_2'])
                else:
                    listdata.append("None")
                key17 = 'organization_domain_2'
                if key17 in content.keys():
                    listdata.append(content['organization_domain_2'])
                else:
                    listdata.append("None")
                listdata.append(str(content['education_1']))
                listdata.append(str(content['education_degree_1']))
                listdata.append(str(content['education_fos_1']))
                listdata.append(str(content['education_start_1']))
                listdata.append(str(content['education_end_1']))
                listdata.append(str(content['education_description_1']))
                listdata.append(str(content['languages']))
                listdata.append(str(content['skills']))
                listdata.append(str(content['twitters']))  
                listdata.append(str(content['phone_1']))
                listdata.append(str(content['phone_type_1']))
                listdata.append(str(content['messenger_1']))
                listdata.append(str(content['messenger_provider_1']))
                key18 = 'messenger_2'
                if key18 in content.keys():
                    listdata.append(content['messenger_2'])
                else:
                    listdata.append("None")
                key19 = 'messenger_provider_2'
                if key19 in content.keys():
                    listdata.append(content['messenger_provider_2'])
                else:
                    listdata.append("None") 
                listdata.append(str(content['website_1']))
                listdata.append(str(content['tags']))
                listdata.append(str(content['note']))
                listdata.append(str(content['connected_at']))
                listdata.append(str(content['mutual_count']))
                listdata.append(str(content['mutual_first_fullname']))
                listdata.append(str(content['mutual_second_fullname']))
                listdata.append(str(content['original_mutual_first_fullname']))
                listdata.append(str(content['original_mutual_second_fullname']))
                listdata.append(str(content['custom_mutual_first_fullname']))
                listdata.append(str(content['custom_mutual_second_fullname']))
                listdata.append(str(content['followers']))
                listdata.append(str(content['member_distance']))
                listdata.append(str(content['network_info_connection_count']))
                listdata.append(str(content['network_info_following']))
                listdata.append(str(content['add_to_target_date']))
                listdata.append(str(content['result_created_at']))
                listdata.append(str(content['message_1_from']))
                listdata.append(str(content['message_1_text']))
                listdata.append(str(content['message_1_send_at']))
                listdata.append(str(content['replied_message_1_from']))
                listdata.append(str(content['replied_message_1_text']))  
                listdata.append(str(content['replied_message_1_send_at']))
                key10 = 'cs_extracted_first_name'
                if key10 in content.keys():
                    listdata.append(content['cs_extracted_first_name'])
                else:
                    listdata.append("None")
                key = 'cs_random-variable'
                if key in content.keys():
                    listdata.append(content['cs_random-variable'])
                else:
                    listdata.append("None")
                listdata.append(str(content['full_messaging_history']))
                listdata.append(str(content['campaign_messaging_history']))
                listdata.append(str(content['last_sent_message_from']))
                listdata.append(str(content['last_sent_message_text']))
                listdata.append(str(content['last_sent_message_send_at']))
                listdata.append(str(content['last_received_message_from']))
                listdata.append(str(content['last_received_message_text']))
                listdata.append(str(content['action_id']))
                listdata.append(str(content['action_name']))
                listdata.append(str(content['action_type']))
                listdata.append(str(content['campaign_id']))
                listdata.append(str(content['campaign_name']))
                listdata.append(str(content['campaign_type']))
                listdata.append(str(content['my_id']))
                listdata.append(str(content['my_email']))
                listdata.append(str(content['my_full_name']))
                keylast = 'last_received_message_send_at'
                if keylast in content.keys():
                    listdata.append(content['last_received_message_send_at'])
                else:
                    listdata.append("None")
                print("WRITING DATA......")
                print(listdata)
                csvfile = open(complete, "a")
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(listdata)
                csvfile.close()
                listdata.clear()

                return 'success', 200 
	else:
            abort(400) 
	
if __name__ == "__main__":
    app.run()
    serve(app, host='0.0.0.0', port=5001)

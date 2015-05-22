"""

return_json_dict = {"result": {"response": 0, 'Type': 'S', 'Msg': 'Alert the user'}}
........................................................................................................................................................

return_json_dict = {"result": {"response": blackboard['rule_output'],
                                               'Type': blackboard['alert_type'],
                                               'Msg': blackboard['alert_msg']}}

---------------------------------------------------------------------------------------------------------------------------------------------------------------
return_json_dict--->

{'result': {'Msg': 'Incomplete Assessment Alert:  All Assessments must be completed at time of episode closure\nError:  Cannot close CM episode with open UM episode attached', 'Type': 'H', 'response': 1}}

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
json.dumps(return_json_dict)---->>

'{"result": {"Msg": "Incomplete Assessment Alert:  All Assessments must be completed at time of episode closure\\nError:  Cannot close CM episode with open UM episode attached", "Type": "H", "response": 1}}'


--------------------------------------------------------------------------------------------------------------------------------------------------------

return_json_dict = {"result": {"response": blackboard['rule_output'],
                                               'Type': blackboard['alert_type'],
                                               'Msg': blackboard['alert_msg']}}
"""
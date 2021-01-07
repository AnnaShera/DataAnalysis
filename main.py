from Api import parse_obj_data, obj_lookup
from args import instance_data_str, volume_data_str


def main():
    # Parse the instance data strings
    instance_obj_list = parse_obj_data(obj_type='instance', data_str=instance_data_str)
    volume_obj_list = parse_obj_data(obj_type='volume', data_str=volume_data_str)

    print('***********************All not terminated instances*********************')

    # All not terminated instances
    prop_dict_running = {'state': 'running'}
    ins_run_list = obj_lookup(instance_obj_list, prop_dict_running)
    prop_dict_stopped = {'state': 'stopped'}
    ins_stop_list = obj_lookup(instance_obj_list, prop_dict_stopped)

    # constructing the running instances list for the volumes part
    run_inst_list = []
    for inst_run in ins_run_list:
        run_inst_list.append(inst_run.id)
        inst_run.print()
    for inst_stop in ins_stop_list:
        inst_stop.print()

    print('*********************All volumes attached to running instances*************')

    # All volumes attached to running instances
    for run_inst_id in run_inst_list:
        filtered_vol_id = obj_lookup(volume_obj_list, {'attached_instance_id': run_inst_id})

        for volume in filtered_vol_id:
            volume.print()


if __name__ == "__main__":
    main()

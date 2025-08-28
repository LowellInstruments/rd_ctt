p = 'ddh:gui:'
RD_DDH_GUI_STATE_EVENT_CODE = p + 'state_gui_event_code'
RD_DDH_GUI_STATE_EVENT_TEXT = p + 'state_gui_event_text'
RD_DDH_GUI_PLOT_REASON = p + 'plot_reason'
RD_DDH_GUI_PLOT_FOLDER = p + 'plot_folder'
p = p + 'refresh:'
RD_DDH_GUI_REFRESH_LOCK_ICON = p + 'lock_icon'
RD_DDH_GUI_REFRESH_NET = p + 'state_process_net'
RD_DDH_GUI_REFRESH_AWS = p + 'state_process_aws'
RD_DDH_GUI_REFRESH_GPS_ANTENNA = p + 'state_antenna_gps'
RD_DDH_GUI_REFRESH_BLE_HISTORY = p + 'state_history'
RD_DDH_GUI_REFRESH_BLE_ANTENNA = p + 'state_antenna_ble'
RD_DDH_GUI_REFRESH_BLE_LAST_DL = p + 'state_last_dl'
RD_DDH_GUI_REFRESH_BLE_ICON_AUTO = p + 'ble_icon'
RD_DDH_GUI_REFRESH_GPS_ICON_AUTO = p + 'gps_icon'
RD_DDH_GUI_REFRESH_CELL_WIFI_ICON_AUTO = p + 'cell_wifi_icon'






p = 'ddh:ble:'
RD_DDH_BLE_RESET_REQ = p + 'linux_reset_req'
RD_DDH_BLE_SEMAPHORE = p + 'semaphore'
RD_DDH_BLE_FINISH_BOOT = p + 'boot'



p = 'ddh:gps:'
RD_DDH_GPS_FIX_POSITION = p + 'fix'
RD_DDH_GPS_FIX_SPEED = p + 'speed'
RD_DDH_GPS_FIX_NUMBER_OF_SATELLITES = p + 'ns_view'
RD_DDH_GPS_COUNTDOWN_FOR_GPS_FIX_AT_BOOT = p + 'time_boot'
RD_DDH_GPS_HAT_GFV = p + 'hat_gfv'
RD_DDH_GPS_FINISH_BOOT = p + 'boot'



p = 'ddh:log:'
RD_DDH_LOG_QUEUE = p + 'queue'
RD_DDH_LOG_FINISH_BOOT = p + 'boot'



p = 'ddh:cnv:'
RD_DDH_CNV_QUEUE = p + 'queue'
RD_DDH_CNV_FINISH_BOOT = p + 'boot'



p = 'ddh:aws:'
RD_DDH_AWS_COPY_QUEUE = p + 'queue'
RD_DDH_AWS_SYNC_REQUEST = p + 'sync'
RD_DDH_AWS_FINISH_BOOT = p + 'boot'



p = 'ddh:sqs:'
RD_DDH_SQS_QUEUE = p + 'queue'
RD_DDH_SQS_FINISH_BOOT = p + 'boot'



p = 'ddh:net:'
RD_DDH_NET_FINISH_BOOT = p + 'boot'



p = 'ddh:slo:'
# to create more smart lock-out entries
RD_DDH_SLO_LS = p + 'ls:'


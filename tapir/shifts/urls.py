from django.urls import path

from tapir.shifts import views

app_name = "shifts"
urlpatterns = [
    path("shift/<int:pk>/", views.ShiftDetailView.as_view(), name="shift_detail"),
    path(
        "shift/<int:pk>/printable",
        views.ShiftDetailView.as_view(
            template_name="shifts/shift_detail_printable.html"
        ),
        name="shift_detail_printable",
    ),
    path(
        "shift/<str:day>/day_printable",
        views.ShiftDayPrintableView.as_view(),
        name="shift_day_printable",
    ),
    path(
        "shift/<int:pk>/edit",
        views.EditShiftView.as_view(),
        name="shift_edit",
    ),
    path(
        "shift_template/<int:pk>/edit",
        views.EditShiftTemplateView.as_view(),
        name="shift_template_edit",
    ),
    path(
        "shift_template/create",
        views.ShiftTemplateCreateView.as_view(),
        name="shift_template_create",
    ),
    path(
        "shift_attendance/<int:pk>/<int:state>",
        views.UpdateShiftAttendanceStateView.as_view(),
        name="update_shift_attendance_state",
    ),
    path(
        "shift_attendance_form/<int:pk>/<int:state>",
        views.UpdateShiftAttendanceStateWithFormView.as_view(),
        name="update_shift_attendance_state_with_form",
    ),
    path(
        "shifttemplate/<int:pk>",
        views.ShiftTemplateDetail.as_view(),
        name="shift_template_detail",
    ),
    path(
        "shifttemplate/overview",
        views.ShiftTemplateOverview.as_view(),
        name="shift_template_overview",
    ),
    path(
        "slottemplate/<int:slot_template_pk>/register",
        views.RegisterUserToShiftSlotTemplateView.as_view(),
        name="slottemplate_register",
    ),
    path(
        "shiftslot/<int:slot_pk>/register/",
        views.RegisterUserToShiftSlotView.as_view(),
        name="slot_register",
    ),
    path(
        "shift_attendance_template/<int:pk>/delete",
        views.shift_attendance_template_delete,
        name="shift_attendance_template_delete",
    ),
    path(
        "calendar",
        views.ShiftCalendarFutureView.as_view(),
        name="calendar_future",
    ),
    path(
        "calendar_past",
        views.ShiftCalendarPastView.as_view(),
        name="calendar_past",
    ),
    path(
        "shift_user_data/<int:pk>",
        views.EditShiftUserDataView.as_view(),
        name="edit_shift_user_data",
    ),
    path(
        "group_calendar",
        views.ShiftTemplateGroupCalendar.as_view(),
        name="shift_template_group_calendar",
    ),
    path(
        "group_calendar/<int:year>",
        views.ShiftTemplateGroupCalendar.as_view(),
        name="shift_template_group_calendar",
    ),
    path(
        "group_calendar/<int:year>/pdf",
        views.ShiftTemplateGroupCalendarAsPdf.as_view(),
        name="calendarpdf",
    ),
    path(
        "shift_account_entry/log/<int:user_pk>",
        views.UserShiftAccountLog.as_view(),
        name="user_shift_account_log",
    ),
    path(
        "shift_account_entry/create/<int:user_pk>",
        views.CreateShiftAccountEntryView.as_view(),
        name="create_shift_account_entry",
    ),
    path(
        "shift_exemption/create/<int:shift_user_data_pk>",
        views.CreateShiftExemptionView.as_view(),
        name="create_shift_exemption",
    ),
    path(
        "shift_exemption/<int:pk>/edit",
        views.EditShiftExemptionView.as_view(),
        name="edit_shift_exemption",
    ),
    path(
        "shift_exemption",
        views.ShiftExemptionListView.as_view(),
        name="shift_exemption_list",
    ),
    path(
        "statistics",
        views.StatisticsView.as_view(),
        name="statistics",
    ),
    path(
        "members_on_alert",
        views.MembersOnAlertView.as_view(),
        name="members_on_alert",
    ),
    path(
        "shift/<int:pk>/cancel",
        views.CancelShiftView.as_view(),
        name="cancel_shift",
    ),
    path(
        "shift/create",
        views.ShiftCreateView.as_view(),
        name="create_shift",
    ),
    path(
        "shift/<int:shift_pk>/slot/create",
        views.ShiftSlotCreateView.as_view(),
        name="create_slot",
    ),
    path(
        "shift_template/<int:shift_pk>/slot_template/create",
        views.ShiftSlotTemplateCreateView.as_view(),
        name="create_slot_template",
    ),
    path(
        "slot/<int:pk>/edit",
        views.ShiftSlotEditView.as_view(),
        name="edit_slot",
    ),
    path(
        "slot_template/<int:pk>/edit",
        views.ShiftSlotTemplateEditView.as_view(),
        name="edit_slot_template",
    ),
]

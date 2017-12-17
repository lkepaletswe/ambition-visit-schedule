from edc_visit_schedule import FormsCollection, Crf

crfs_d1 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.patienthistory'),
    Crf(show_order=2, model='ambition_subject.medicalexpenses'),
    Crf(show_order=3, model='ambition_subject.medicalexpensestwo',
        required=False),
    Crf(show_order=4, model='ambition_subject.education'),
    Crf(show_order=5, model='ambition_subject.educationhoh', required=False),
    Crf(show_order=6, model='ambition_subject.bloodresult'),
    Crf(show_order=7, model='ambition_subject.lumbarpuncturecsf'),
    Crf(show_order=8, model='ambition_subject.pkpdcrf'),
    Crf(show_order=9, model='ambition_subject.prnmodel'),
    Crf(show_order=10, model='ambition_subject.microbiology', required=False),
    Crf(show_order=11, model='ambition_subject.radiology', required=False),
    name='day1'
)

crfs_d3 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.bloodresult'),
    Crf(show_order=2, model='ambition_subject.prnmodel'),
    Crf(show_order=3, model='ambition_subject.microbiology', required=False),
    Crf(show_order=4, model='ambition_subject.radiology', required=False),
    Crf(show_order=5, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    name='day3'
)

crfs_d5 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.bloodresult'),
    Crf(show_order=2, model='ambition_subject.prnmodel'),
    Crf(show_order=3, model='ambition_subject.microbiology', required=False),
    Crf(show_order=4, model='ambition_subject.radiology', required=False),
    Crf(show_order=5, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    name='day5'
)

crfs_d7 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.bloodresult'),
    Crf(show_order=2, model='ambition_subject.lumbarpuncturecsf'),
    Crf(show_order=3, model='ambition_subject.prnmodel'),
    Crf(show_order=4, model='ambition_subject.microbiology', required=False),
    Crf(show_order=5, model='ambition_subject.radiology', required=False),
    Crf(show_order=6, model='ambition_subject.pkpdcrf'),
    name='day7'
)

crfs_d10 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.bloodresult'),
    Crf(show_order=2, model='ambition_subject.prnmodel'),
    Crf(show_order=3, model='ambition_subject.microbiology', required=False),
    Crf(show_order=4, model='ambition_subject.radiology', required=False),
    Crf(show_order=5, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    name='day10'
)

crfs_d12 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.bloodresult'),
    Crf(show_order=2, model='ambition_subject.prnmodel'),
    Crf(show_order=3, model='ambition_subject.microbiology', required=False),
    Crf(show_order=4, model='ambition_subject.radiology', required=False),
    Crf(show_order=5, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    name='day12'
)

crfs_d14 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.bloodresult'),
    Crf(show_order=2, model='ambition_subject.lumbarpuncturecsf'),
    Crf(show_order=3, model='ambition_subject.week2'),
    Crf(show_order=4, model='ambition_subject.prnmodel'),
    Crf(show_order=5, model='ambition_subject.microbiology', required=False),
    Crf(show_order=6, model='ambition_subject.radiology', required=False),
    Crf(show_order=7, model='ambition_subject.pkpdcrf'),
    name='day14'
)

crfs_w4 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.week4'),
    Crf(show_order=2, model='ambition_subject.bloodresult'),
    Crf(show_order=3, model='ambition_subject.prnmodel'),
    Crf(show_order=4, model='ambition_subject.microbiology', required=False),
    Crf(show_order=5, model='ambition_subject.radiology', required=False),
    Crf(show_order=6, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    name='week4'
)

crfs_w6 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.followup'),
    Crf(show_order=3, model='ambition_subject.prnmodel'),
    Crf(show_order=4, model='ambition_subject.bloodresult', required=False),
    Crf(show_order=5, model='ambition_subject.microbiology', required=False),
    Crf(show_order=6, model='ambition_subject.radiology', required=False),
    Crf(show_order=7, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    name='week6'
)

crfs_w8 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.followup'),
    Crf(show_order=3, model='ambition_subject.prnmodel'),
    Crf(show_order=4, model='ambition_subject.bloodresult', required=False),
    Crf(show_order=5, model='ambition_subject.microbiology', required=False),
    Crf(show_order=6, model='ambition_subject.radiology', required=False),
    Crf(show_order=7, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    name='week8'
)

crfs_w10 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.followup'),
    Crf(show_order=2, model='ambition_subject.medicalexpenses'),
    Crf(show_order=3, model='ambition_subject.medicalexpensestwo'),
    Crf(show_order=4, model='ambition_subject.prnmodel'),
    Crf(show_order=5, model='ambition_subject.bloodresult', required=False),
    Crf(show_order=6, model='ambition_subject.microbiology', required=False),
    Crf(show_order=7, model='ambition_subject.radiology', required=False),
    Crf(show_order=8, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    name='week10'
)

crfs_w16 = FormsCollection(
    Crf(show_order=1, model='ambition_subject.week16'),
    name='week16'
)

crfs_unscheduled = FormsCollection(
    Crf(show_order=1, model='ambition_subject.prnmodel'),
    Crf(show_order=2, model='ambition_subject.bloodresult',
        required=False),
    Crf(show_order=3,
        model='ambition_subject.microbiology', required=False),
    Crf(show_order=4, model='ambition_subject.radiology',
        required=False),
    Crf(show_order=5, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    name='unscheduled'
)

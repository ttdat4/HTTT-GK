# coding=utf8
from openerp.osv import fields,osv

class quanlyhp (osv.osv):
    _name='quanlyhp.quanlyhp'
    _columns = {
        # cac thuoc tinh cua lop danh muc hoc phan
        'name': fields.char('Học phần', size=25, required=True),
        'sotinchi': fields.integer('Số tín chỉ', required=True),
        'hocphantienquyet': fields.selection([('ltcb', 'Lập trình cơ bản'), ('ctdl', 'Cấu trúc dữ liệu'),
                                             ('ltnc', 'Lập trình nâng cao'), ('th', 'Tin Học')], 'Học phần tiên quyết'),

        
        'tienquyet':fields.many2many('quanlyhp.quanlyhp','hocphan_tienquyet_rel', 'hocphan_id','tienquyet_id',"Học phần tiên quyết")
    }
    _defaults = {
        'sotinchi': 1
    }


class lophocphan(osv.osv):
    _name = 'quanlyhp.lophocphan'
    _columns = {
        'malophocphan': fields.char('Mã lớp học phần', size=25, required=True),
        'tenhocphan': fields.many2one('quanlyhp.quanlyhp', "Tên học phần", help="Học phần",required=True),
        'giangvien': fields.selection([('ttd', 'Trần Thành Đạt'), ('ddt', 'Đạt Đẹp Trai'), ('ddn', "Đạt Đồng Nai")], 'Giảng viên',required=True),
        'ngaybatdau': fields.datetime('Ngày bắt đầu'),
        'ngayketthuc': fields.datetime('Ngày kết thúc'),
        'thongtin': fields.text('Thông tin')
    }
quanlyhp()

lophocphan()

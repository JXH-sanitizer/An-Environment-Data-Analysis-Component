from flask import Blueprint,render_template,redirect,request, url_for
from exts import db
from apps.pollution.model import Pollution
from cas import cases

pol_bp = Blueprint('pol',__name__,url_prefix='/pollution')

@pol_bp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        cas = request.form.get('CAS')
        name = request.form.get('name')
        location = request.form.get('location')
        unit = request.form.get('unit')
        conc = request.form.get('conc')
        df = cases()
        name_df = df.iloc[:,0]
        cas_df = df.iloc[:,1]
        if sum(name_df == name) == 0 and sum(cas_df == cas) == 0:
            pollutant = Pollution()
            pollutant.CAS = cas
            pollutant.location = location
            pollutant.pollutionname = name
            pollutant.unit = unit
            pollutant.conc = conc
            db.session.add(pollutant)
            db.session.commit()
            return render_template('pollution/register.html')
        elif sum(name_df == name) != 0 and sum(cas_df == cas) == 0:
            return 'CAS号与污染物名称不匹配!'
        elif sum(name_df == name) == 0 and sum(cas_df == cas) != 0:
            return 'CAS号与污染物名称不匹配!'
        elif sum(name_df == name) != 0 and sum(cas_df == cas) != 0:
            this_pollutant = df[df.iloc[:,0] == name]
            if name == this_pollutant.iloc[0,0] and cas == this_pollutant.iloc[0,1]:
                pollutant = Pollution()
                pollutant.CAS = cas
                pollutant.location = location
                pollutant.pollutionname = name
                pollutant.unit = unit
                pollutant.conc = conc
                db.session.add(pollutant)
                db.session.commit()
                return render_template('pollution/register.html')
            else:
                return 'CAS号与污染物名称不匹配!'
        else:
            return 'CAS号与污染物名称不匹配!'
    else:
        return render_template('pollution/register.html')
    
@pol_bp.route('/show',methods=['GET','POST'])
def show():
    pollutants = Pollution.query.filter(Pollution.isdelete==0).all()
    return render_template('pollution/show.html',pollutants = pollutants)

@pol_bp.route('/delete')
def delete():
    id = request.args.get('id')
    pollutant = Pollution.query.get(id)
    pollutant.isdelete = True
    db.session.commit()
    return redirect(url_for('pol.show'))

@pol_bp.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        id = request.form.get('id')
        cas = request.form.get('CAS')
        name = request.form.get('name')
        location = request.form.get('location')
        unit = request.form.get('unit')
        conc = request.form.get('conc')
        pollutant = Pollution.query.get(id)
        pollutant.CAS = cas
        pollutant.location = location
        pollutant.pollutionname = name
        pollutant.unit = unit
        pollutant.conc = conc
        db.session.commit()
        return redirect(url_for('pol.show'))
    else:
        id = request.args.get('id')
        pollutant = Pollution.query.get(id)
        return render_template('pollution/update.html',pollutant = pollutant)

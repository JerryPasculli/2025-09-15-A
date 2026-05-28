from database.DB_connect import DBConnect
from model.nodo import Nodo


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results



    @staticmethod
    def getNodi(primo, secondo):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """with id as (select d.driverId
from drivers d, results r, races r1
where d.driverId = r.driverId and r.raceId = r1.raceId and position is not null
and year between %s and %s
group by d.driverId)

select d.*
from drivers d where driverId in (select * from id)"""

        cursor.execute(query, [primo, secondo])

        for row in cursor:
            results.append(Nodo(**row))

        cursor.close()
        conn.close()
        return results


    @staticmethod
    def getArchi(primo, secondo):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor()
        query = """with costruttori as (select d.driverId, r.constructorId, r.raceId
from drivers d, results r, races r1
where d.driverId = r.driverId and r.raceId = r1.raceId and position is not null
and year between %s and %s
group by d.driverId, r.constructorId, r.raceId)

select c1.driverId, c2.driverId, count(distinct c1.raceId) as peso
from costruttori c1, costruttori c2
where c1.driverId>c2.driverId and c1.constructorId = c2.constructorId and 
c1.raceId = c2.raceId
group by c1.driverId, c2.driverId"""

        cursor.execute(query, [primo, secondo])

        for row in cursor:
            results.append(row)

        cursor.close()
        conn.close()
        return results




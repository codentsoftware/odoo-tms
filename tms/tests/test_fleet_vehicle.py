# -*- coding: utf-8 -*-
# Copyright 2017, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from datetime import datetime, timedelta

from odoo.tests.common import TransactionCase


class TestFleetVehicle(TransactionCase):

    def setUp(self):
        super(TestFleetVehicle, self).setUp()
        self.unit = self.env.ref('tms.tms_fleet_vehicle_02')

    def test_10_fleet_vehicle_compute_insurance_days_to_expire(self):
        date = datetime.now() + timedelta(days=10)
        self.unit.write({
            'insurance_expiration': date})
        self.assertEqual(self.unit.insurance_days_to_expire, 10)

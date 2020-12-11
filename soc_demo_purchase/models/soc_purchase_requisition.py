from odoo import api, fields, models


class SocPurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    candidate_ids = fields.Many2many('res.partner', string='Candidates')

    @api.model
    def create(self, vals):
        """
        Inherit standard method to add the partners in the field 'candidate_ids' to the followers
        """
        res = super().create(vals)

        res.message_subscribe(res.candidate_ids.ids)

        return res

    def write(self, vals):
        """
        Inherit standard method to synchronize the field 'candidate_ids' with the followers
        """
        if 'candidate_ids' in vals:
            candidates_ids = vals.get('candidate_ids', False)
            if candidates_ids and candidates_ids[0] and len(candidates_ids[0]) == 3:
                updated_candidates = candidates_ids[0][2]
                self._add_candidates_to_followers(updated_candidates)
                self._remove_candidates_from_followers(updated_candidates)

        return super().write(vals)

    def _add_candidates_to_followers(self, updated_candidates):
        """
        Method to add partners from list 'updated_candidates', which
        are not in the field 'candidate_ids', to the list of followers
        """
        for requisition in self:
            new_followers = []
            current_candidates = requisition.candidate_ids.ids
            for updated_candidate_id in updated_candidates:
                if updated_candidate_id not in current_candidates:
                    new_followers.append(updated_candidate_id)

            requisition.message_subscribe(new_followers)

    def _remove_candidates_from_followers(self, updated_candidates):
        """
        Method to remove partners from field 'candidate_ids', which are
        not in the list 'updated_candidates', to the list of followers
        """
        for requisition in self:
            old_followers = []
            current_candidates = requisition.candidate_ids.ids
            for current_candidate_id in current_candidates:
                if current_candidate_id not in updated_candidates:
                    old_followers.append(current_candidate_id)

            requisition.message_unsubscribe(old_followers)

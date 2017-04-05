/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
	listNode ans(0);
	listNode *node = &ans;
	int extra = 0;
	
	while (l1 || l2 || extra) {
		int l1Value = 0;
		int l2Value = 0;
		if (l1 ) {
			l1Value = l1->val;
			l1 = l1->next;
		}
		if (l2 ) {
			l2Value = l2->val;
			l2 = l2->next;
		}
		nede->next = new ListNode((l1Value + l2Value + extra) % 10);
		extra = (l1Value + l2Value + extra) / 10;
		node = node -> next;
	}
	return ans.next;
    }
};

void main(){

    // Definition for singly-linked list.
    struct ListNode {
        int val;
        struct ListNode *next;
    };

    struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2)
    {
        if (!l1->next)
            return l2;
        else
            return l1;
        
        if (l1->val <= l2->val){
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        }
        else{
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    };

    struct ListNode l11;
    struct ListNode l12;
    struct ListNode l21;
    struct ListNode l22;
    struct ListNode *merged;

    l11.val = 1;
    l11.next = &l12;
    l12.val = 2;

    l21.val = 3;
    l21.next = &l22;
    l22.val = 4;

    merged = mergeTwoLists(&l11, &l21);
    printf(merged);
}


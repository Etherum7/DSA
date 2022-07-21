class Solution:
    # Function to merge K sorted linked list.
    def mergeKLists(self, arr, K):
        # code here
        # return head of merged list
        # print(arr)
        head = Node(0)
        temp = head
        heap = []
        for ind, node in enumerate(arr):
            heappush(heap, (node.data, ind, node))
        while(len(heap)):
            node = heappop(heap)
            # print(node[1].data)

            temp.next = node[2]
            temp = temp.next
            if node[2].next:
                heappush(heap, (node[2].next.data, node[1], node[2].next))
        return head.next

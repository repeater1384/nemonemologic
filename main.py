class NemoNemoLogic:

    def __init__(self, size, col_info, row_info):
        self.size = size
        self.col_info = col_info
        self.row_info = row_info

    def solve(self):
        pass

    def one_line_init(self, line_info):  # 초기 정보로 반드시 칠해질수 있는칸 채우기
        state = [0] * self.size
        sum_space_painted = sum(line_info) + len(line_info) - 1
        total_blanked = self.size - sum_space_painted

        cur_idx = total_blanked
        for info in line_info:
            if info >= total_blanked:
                for _ in range(info - total_blanked):
                    state[cur_idx] = 1
                    cur_idx += 1

            cur_idx += total_blanked + 1
        return state

    def all_line_init(self):
        # matrix = [[0]*self.size for _ in range(self.size)]
        matrix = []
        for row in self.row_info:
            inited_data = self.one_line_init(row)
            matrix.append(inited_data)

        for idx, col in enumerate(self.col_info):
            inited_data = self.one_line_init(col)
            for r, i in zip(range(self.size), inited_data):
                if matrix[r][idx] == 0:
                    matrix[r][idx] = i
        print(*matrix, sep='\n')


if __name__ == '__main__':
    nemologic = NemoNemoLogic(5, [[3], [1, 1], [2, 1], [4], [3]], [[1], [3], [1, 2], [1, 2], [5]])
    nemologic.all_line_init()

def split_in_two(integer):
    len_of_int = int(len(integer)/2)
    split_int = [int(integer[0:len_of_int]),int(integer[len_of_int:])]

    return split_int

def ChallengePart_1():
    # input_ids = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224','1698522-1698528','446443-446449','38593856-38593862','565653-565659','824824821-824824827','2121212118-2121212124']
    input_ids = open('Day 2/input.txt', 'r').readline().split(',')
    invalid_id_list = []

    for id_range in input_ids:
        start_id = id_range.split("-")[0]
        end_id = id_range.split("-")[1]

        for count in range(int(start_id),int(end_id)+1):
            if len(str(count))%2 == 0:
                checked_seqs = split_in_two(str(count))
                if checked_seqs[0] == checked_seqs[1]:
                    invalid_id_list.append(count)

    # print(sum(invalid_id_list)==1227775554)
    print(f"The sum of invalid ID sequnaces is {sum(invalid_id_list)}")

def main():

    ChallengePart_1()
    # ChallengePart_2()
    

if __name__ == "__main__":
    main()
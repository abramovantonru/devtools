uses Crt;

const
   N = 4; // ���������� ��������
   M = 5; // ������ (� ���.)
   
type
   Table = record // �������:{ �����, ����:[] }
      Sum: real;
      Plan: array[1..N] of real;
   end;

//����������
const Profitability: array[0..M, 1..N] of real = (
        (0.00, 0.00, 0.00, 0.00),
        (0.28, 0.25, 0.15, 0.20),
        (0.23, 0.21, 0.13, 0.18),
        (0.22, 0.18, 0.13, 0.14),
        (0.20, 0.16, 0.13, 0.12),
        (0.18, 0.15, 0.12, 0.11)
    );

var
    Income: array[0..M, 1..N] of real; // �����
    Optimal: array[0..M, 1..N] of Table; // ����������� �����
    Best: array [0..M] of real; // ����� �����������
    maxI: integer;  // ������ �������������
    answerIncome :string; // ������ ������ c �������
    
begin
    writeln();
    writeln('������������� ������������ ����� ���������� ������� ��������.');
    writeln();

    for var i := 0 to M do begin
        for var k := 1 to N do begin
            Income[i,k] := Profitability[i,k] * i;
            end;
        end;
         
    for var i := 0 to M do begin
        for var k := 1 to N do begin
            Optimal[i,k].Sum := 0;
            for var j := 1 to N do 
                Optimal[i,k].Plan[j] := 0;
            end;
         end;
         
    for var i:=0 to M do begin
        Optimal[i,1].Sum := Income[i,1];
        Optimal[i,1].Plan[1] := i;
        end;
         
    for var i := 0 to M do begin
        for var k := 2 to N do begin
            for var j := 0 to i do begin
                Best[j] := Optimal[j,k-1].Sum + Income[i-j,k];
                end;
               
            maxI:=0;
            
            for var j := 0 to i do begin
                if (Best[j] > Best[maxI]) then
                    maxI:=j;
                end;

            Optimal[i,k].Sum := Best[maxI];
            Optimal[i,k].Plan := Optimal[maxI,k-1].Plan;
            Optimal[i,k].Plan[k] := i - maxI;
            end;
         end;
     
    writeln('����������� ���� ����������:');
    writeln('------------------------------');
    
    for var i:=1 to N do begin
        writeln('� ������ �' + IntToStr(i) + ' ������������� ' + IntToStr(round(Optimal[M,N].Plan[i])) + '���.');
        end;
   
    writeln('------------------------------');
    str(Optimal[M,N].Sum:5:2, answerIncome);
    writeln('����������� �������� �����: ' + answerIncome + ' ���.');
end.
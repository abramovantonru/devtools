using System;

namespace mm{
	class Program{
		const int N = 4;
		const int M = 5;

		public class Table {
			private double _sum = 0.0;
			private double[] _plan = { 0.0, 0.0, 0.0, 0.0 };
			
			public double Sum {
				get {
					return _sum;
				}
				set {
					this._sum = value;
				}
			}

			public double[] Plan{
				get{
					return _plan;
				}
				set{
					this._plan = value;
				}
			}

			public double getPlan(int index) {
				return this._plan[index];
			}

			public void setPlan(int index, double value) {
				this._plan[index] = value;
			}
		}

		public double[,] Income = new double[M + 1, N]; 

		public readonly double[,] Profitability = { 
			{ 0.00, 0.00, 0.00, 0.00 }, 
			{ 0.28, 0.25, 0.15, 0.20 }, 
			{ 0.23, 0.21, 0.13, 0.18 },
			{ 0.22, 0.18, 0.13, 0.14 },
			{ 0.20, 0.16, 0.13, 0.12 },
			{ 0.18, 0.15, 0.12, 0.11 }
		};

		public Table[,] Optimal = new Table[M + 1, N];
		public double[] Best = new double[M + 1];
		int maxI;

		public void begin(){
			for(int i = 0; i <= M; i++)
				for(int j = 0; j < N; j++)
					Optimal[i, j] = new Table();
				
			Console.WriteLine();
			Console.WriteLine("Моделирования оптимального плана инвестиций методом Беллмана.");
			Console.WriteLine();

			for (int i = 0; i <= M; i++)
				for (int j = 0; j < N; j++)
					Income[i, j] = Profitability[i, j] * i;
			
			for (int i = 0; i <= M; i++){
				Optimal[i, 0].Sum = Income[i, 0];
				Optimal[i, 0].setPlan(0, i);
			}

			for (int i = 0; i <= M; i++){
				for (int j = 1; j < N; j++){
					for (int k = 0; k <= i; k++)
						Best[k] = Optimal[k, j - 1].Sum + Income[i - k, j];

					maxI = 0;

					for (int k = 0; k <= i; k++)
						if (Best[k] > Best[maxI])
							maxI = k;

					Optimal[i, j].Sum = Best[maxI];
					Optimal[i, j].Plan = Optimal[maxI, j - 1].Plan;
					Optimal[i, j].setPlan(j, i - maxI);
				}
			}

			Console.WriteLine("Оптимальный план инвестиций:");
			Console.WriteLine("-------------------------------");
			
			for (int i = 0; i < N; i++)
				Console.WriteLine("В проект № " + (i + 1) + " инвестировать " + Math.Round(Optimal[M, N - 1].getPlan(i)).ToString() + "млн.");

			Console.WriteLine("-------------------------------");
			Console.WriteLine("Планируется получить доход: " + Optimal[M, N - 1].Sum + " млн.");
			Console.ReadKey();
		}

		static void Main(string[] args){
			var app =  new Program();
			app.begin();
		}
	}
}

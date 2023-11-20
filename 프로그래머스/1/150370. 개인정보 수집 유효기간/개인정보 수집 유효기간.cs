using System;
using System.Collections.Generic;
public class Solution {
   public List<int> solution(string today, string[] terms, string[] privacies)
        {
            today = (today.Replace(".", string.Empty));

            int today_yy = Int32.Parse(today.Substring(2, 2));
            int today_MM = Int32.Parse(today.Substring(4, 2));
            int today_dd = Int32.Parse(today.Substring(6, 2));
            string[] terms_kind = new string[terms.Length];
            for (int i = 0; i < terms.Length; i++)
            {
                terms_kind[i] = terms[i][0].ToString();
            }
            int num = 1;
            List<int> answer = new List<int>();
            foreach (string _pr in privacies)
            {
                
                string _kind = _pr[11].ToString();

                int idx = Array.IndexOf(terms_kind, _kind);

                int period = Int32.Parse(terms[idx].Substring(2));

                string Re_pr = _pr.Replace(".", string.Empty);
                int _yy = Int32.Parse(Re_pr.Substring(2, 2));
                int _MM = Int32.Parse(Re_pr.Substring(4, 2));
                int _dd = Int32.Parse(Re_pr.Substring(6, 2));

                if (_MM + period > 12)
                {
                    if ((_MM + period) % 12 == 0)
                    {
                        _yy += ((_MM + period) / 12 ) -1;
                        _MM = 12;
                    }
                    else
                    {
                        _yy += (_MM + period) / 12;
                        _MM = (_MM + period) % 12;
                    }
                }
                else
                {
                    _MM = _MM + period;
                }

                if(today_yy > _yy)
                {
                    answer.Add(num);
                }
                else if(today_yy == _yy && today_MM > _MM)
                {
                    answer.Add(num);
                }
                else if(today_yy == _yy && today_MM == _MM && today_dd >= _dd)
                {
                    answer.Add(num);
                }
                
                num++;
            }

            return answer;
        }
}
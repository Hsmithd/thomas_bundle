# Play: Lemon - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "lemon_app"
    retry_count: 1

  tasks:
    - name: Ensure hazel-task-1 is present
      ansible.builtin.file:
        path: /opt/lemon/hazel-task-1
        state: directory

    - name: Template hazel-task-1 config
      ansible.builtin.template:
        src: templates/hazel-task-1.j2
        dest: /etc/lemon/hazel-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart lemon service
      ansible.builtin.service:
        name: lemon
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:43Z
